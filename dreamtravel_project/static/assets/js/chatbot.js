document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('input-form');
    const inputField = document.getElementById('input-field');
    const conversation = document.getElementById('conversation');

    // Fonction pour soumettre le formulaire sans rechargement de page
    form.addEventListener('submit', askQuestion);

    function askQuestion(event) {
        event.preventDefault(); // Empêche le rechargement de la page

        const question = inputField.value.trim();

        if (question === "") {
            return; // Ne rien faire si le champ est vide
        }

        displayUserMessage(question); // Afficher le message de l'utilisateur
        sendQuestionToServer(question); // Envoyer la question au serveur

        inputField.value = ""; // Effacer le champ d'entrée
    }

    function displayUserMessage(text) {
        const userDiv = document.createElement('div');
        userDiv.className = 'chatbot-message user-message';
        userDiv.innerHTML = `<p class="chatbot-text">${text}</p>`;
        conversation.appendChild(userDiv);
        scrollConversationToEnd(); // Défiler jusqu'à la fin
    }

    function displayBotResponse(text) {
        const botDiv = document.createElement('div');
        botDiv.className = 'chatbot-message chatbot-message';
        botDiv.innerHTML = `<p class="chatbot-text">${text}</p>`;
        conversation.appendChild(botDiv);
        scrollConversationToEnd(); // Défiler jusqu'à la fin
    }

    function sendQuestionToServer(text) {
        const csrfToken = getCookie('csrftoken'); // Utiliser le token CSRF du cookie

        $.ajax({
            type: 'POST',
            url: '/ask_question/', // Assurez-vous que c'est la bonne URL
            data: {
                text: text,
                csrfmiddlewaretoken: csrfToken // Inclure le token CSRF
            },
            success: function(response) {
                if (response && response.data) {
                    displayBotResponse(response.data.text);
                } else {
                    displayBotResponse('No response data received.');
                }
            },
            error: function() {
                displayBotResponse('Sorry, there was an error processing your request.');
            }
        });
    }

    function scrollConversationToEnd() {
        conversation.scrollTop = conversation.scrollHeight; // Défiler jusqu'à la fin
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=') && name === 'csrftoken') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
