from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        # Configure Google Generative AI
        genai.configure(api_key="VOTRE_API_KEY")

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
        ]

        system_instruction = "Vous êtes un chatbot pour un site web de tourisme au Maroc. Répondez aux questions des clients et donnez des recommandations."

        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config=generation_config,
            system_instruction=system_instruction,
            safety_settings=safety_settings,
        )

        response = model.generate_content(user_input)
        chatbot_response = ''.join([p.text for p in response.candidates[0].content.parts])

        return JsonResponse({"chatbot_response": chatbot_response})

    return JsonResponse({"error": "Invalid request method"}, status=400)
