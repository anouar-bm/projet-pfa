from django.shortcuts import render , redirect
import requests
from django.template import TemplateDoesNotExist
from bs4 import BeautifulSoup
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import csv
import json
from django.urls import path
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from app_siteweb.models import Hotel, Image
from decimal import Decimal
from django.core.files.base import ContentFile
import os





from django.shortcuts import render, redirect
from playwright.sync_api import sync_playwright
from django.http import HttpResponse
from decimal import Decimal
from app_siteweb.models import Hotel, Image  # Adjust based on your app's name
import os
from django.core.files.base import ContentFile
import pandas as pd

def scrape(request):
    if request.method == 'POST':
        try:
            with sync_playwright() as p:
                checkin_date = '2024-06-24'  # You can make these dynamic
                checkout_date = '2024-06-28'
                
                page_url = f'https://www.booking.com/searchresults.es.html?ss=Marrakech&checkin={checkin_date}&checkout={checkout_date}'
                browser = p.chromium.launch(headless=True)  # Set to False if you want to see the browser
                page = browser.new_page()
                page.goto(page_url, timeout=60000)  # Adjust timeout
                
                # Find all hotels
                hotel_elements = page.locator('//div[@data-testid="property-card"]').all()
                
                for hotel_element in hotel_elements:
                    # Extract hotel information
                    nom = hotel_element.locator('//div[@data-testid="title"]').inner_text(strip=True)
                    emplacement = hotel_element.locator('//span[@data-testid="property-card__address"]').inner_text(strip=True)
                    
                    # Default description
                    description = 'Aucune description fournie'
                    
                    # Extract price and promotion
                    prix_element = hotel_element.locator('//span[@data-testid="price-and-discounted-price"]').inner_text(strip=True)
                    prix = Decimal(prix_element.replace("MAD", "").replace("\u00a0", ""))
                    
                    promo = 0
                    promo_element = hotel_element.locator('//span[@data-testid="price-and-discounted-price__old-price"]')
                    if promo_element:
                        prix_avec_promo = Decimal(promo_element.inner_text(strip=True).replace("MAD", "").replace("\u00a0", ""))
                        if prix_avec_promo > prix:
                            promo = ((prix_avec_promo - prix) / prix_avec_promo) * 100
                    
                    # Create or update the Hotel model
                    hotel, created = Hotel.objects.update_or_create(
                        nom=nom,
                        defaults={
                            'emplacement': emplacement,
                            'description': description,
                            'prix': prix,
                            'promo': promo
                        }
                    )
                    
                    # Extract and save images
                    image_elements = hotel_element.locator('//img').all()  # Adjust if necessary
                    for img in image_elements:
                        img_url = img.get('src')
                        if img_url:
                            img_resp = requests.get(img_url)
                            if img_resp.status_code == 200:
                                img_name = os.path.basename(img_url)
                                new_image = Image()
                                new_image.image.save(img_name, ContentFile(img_resp.content), save=True)
                                hotel.photos.add(new_image)

                # Close the browser
                browser.close()

            return redirect('scraping_app:scrape_results')  # Redirect to the results page
        except Exception as e:
            return render(request, 'scrap/home.html', {'error': f"An error occurred: {e}"})
    else:
        return render(request, 'scrap/home.html')








def home(request):
    return render(request, 'scrap/home.html')




def scrape_results(request):
    try:
        hotels = Hotel.objects.all()  # Retrieve all hotels
        return render(request, 'scrap/result.html', {'hotels': hotels})
    except TemplateDoesNotExist as e:
        return HttpResponse(f"Template not found: {e}")
    
def download_file(request):
    if 'scraped_data' in request.session:
        context = request.session['scraped_data']
        response = HttpResponse(content_type='')
        if request.POST['download_type'] == 'pdf':
            template_path = 'result.html'
            template = get_template(template_path)
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            filename = f"{context['title']}.pdf"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf-8')
            if pisa_status.err:
                return HttpResponse('PDF generation failed')
        elif request.POST['download_type'] == 'csv':
            response = HttpResponse(content_type='text/csv')
            filename = f"{context['title']}.csv"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            writer = csv.writer(response)
            writer.writerow(['Title', 'Headings', 'Paragraphs'])
            rows = zip([context['title']], context['headings'], context['paragraphs'])
            for row in rows:
                writer.writerow(row)
        elif request.POST['download_type'] == 'json':
            response = HttpResponse(content_type='application/json')
            filename = f"{context['title']}.json"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            json.dump(context, response, indent=4)
        return response
    else:
        return render(request, 'scrap/home.html')