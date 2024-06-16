import ollama as ollama


class OllamaClient:
    def __init__(self):
        print('Init OllamaClient')

    def get_response(self, content: str, subject: str, name: str):

        is_a_subject = self.__is_subject(subject.strip())
        # print('Is a subject: ', is_a_subject)

        is_a_softskill = self.__is_softskill(content)
        # print('Is a softskill: ', is_a_softskill)

        if is_a_subject is True or is_a_softskill is True:

            messages = self.__get_message_history(subject)

            if is_a_softskill:
                messages.append({'role': 'user', 'content': content})
            else:
                messages.append({'role': 'user', 'content': subject + ': ' + content})
            options = {
                'temperature': 0.2,
            }

            response = ollama.chat(
                model='llama3',
                messages=messages,
                options=options)

            reply = response['message']['content']

            return reply

        else:
            return content

    def __is_subject(self, phrase: str):
        content = f"Ist das Wort '{phrase}' ein Schulfach? Antworte nur mit den Wörtern Ja oder Nein, ohne Satzzeichen."
        yes_no = self.__is_yes(content)
        return yes_no

    def __is_softskill(self, phrase: str):
        content = (f"Handelt es sich bei der Phrase '{phrase}' um eine soziale Kompetenz wie hilfsbereit, teamfähig, "
                   f"konfliktfähigoder, analytisches Denken still im Unterricht. "
                   f"Antworte mit Ja oder Nein, ohne Satzzeichen.")
        yes_no = self.__is_yes(content)
        return yes_no

    def __is_yes(self, content: str):
        # print(content)
        messages = [{'role': 'system', 'content': self.__get_sys_prompt()}, {'role': 'user', 'content': content}]

        options = {
            'temperature': 0.2,
        }

        response = ollama.chat(
            model='llama3',
            messages=messages,
            options=options)

        reply = response['message']['content']

        reply = reply.lower()
        # print(reply)

        return reply in ['ja', 'yes', 'y', 'j']

    def __get_sys_prompt(self):
        return (
                "Antworte immer auf Deutsch. Rolle: Du bist ein AI-Assistent, der Bemerkungstexte für Grundschulzeugnisse "
                "erstellt oder korrigiert. "
                "Deine Aufgabe ist es, aus kurzen stichwortartigen Sätzen ausführliche und positive Texte zu formulieren. "
                "Diese Texte sollen die Schülerinnen und Schüler direkt ansprechen, wertschätzend sein und ihre "
                "individuellen Leistungen und Fortschritte hervorheben."
                "Ziel: Erstelle oder korrigiere Bemerkungstexte, die motivierend und ermutigend sind, die Stärken der "
                "Schülerinnen und Schüler betonen und konstruktives Feedback geben. "
                "Die Texte sollen in klarer, freundlicher und positiver Sprache verfasst sein."
                "Anweisungen:" +
                "Ausführlichkeit: Verwandle kurze stichwortartige Sätze in vollständige, ausführliche Bemerkungstexte."
                "Direkte Ansprache: Sprich die Schülerin oder den Schüler "
                "direkt an (z.B. \"Du hast...\" oder \"Deine Leistung in...\")."
                "Positiver Ton: Betone stets die positiven Aspekte und Stärken des Schülers oder der Schülerin. "
                "Negative Aspekte sollen behutsam und konstruktiv angesprochen werden."
                "Individuelle Würdigung: Gehe auf individuelle Leistungen und Fortschritte ein und vermeide allgemeine "
                "oder standardisierte Aussagen.")

    def __get_message_history(self, subject: str):
        faecherNormal = ['Mathematik', 'Mathe', 'Deutsch', 'Englisch', 'Geographie', 'Physik', 'Chemie', 'Erdkunde',
                         'Informatik', 'Geschichte', 'Sachunterricht']
        faecherAndere = ['Kunst', 'Musik', 'Sport', 'Theater', 'Darstellendes Spiel']

        messages = [{'role': 'system', 'content': self.__get_sys_prompt()}]

        if subject in faecherNormal:
            #print('Baue History mit Fach Normal: ' + subject)
            userGut = 'XYZ: gut'
            userGut = userGut.replace('XYZ', subject)
            assistenGut = 'In XYZ hast du bemerkenswerte Fortschritte gemacht und zeigst ein gutes Veröffnis der Themen. '
            assistenGut = assistenGut.replace('XYZ', subject)
            messages.append({'role': 'user', 'content': userGut})
            messages.append({'role': 'assistant', 'content': assistenGut})
            userAktiv = 'XYZ: aktiv'
            userAktiv = userAktiv.replace('XYZ', subject)
            assistenAktiv = 'Im XYZunterricht bist du sehr aktiv und beteiligst dich gerne am Unterrichtsgeschehen.'
            assistenAktiv = assistenAktiv.replace('XYZ', subject)
            messages.append({'role': 'user', 'content': userAktiv})
            messages.append({'role': 'assistant', 'content': assistenAktiv})
            userVerbessert = 'XYZ: verbessert'
            userVerbessert = userVerbessert.replace('XYZ', subject)
            assistenVerbessert = 'Deine Fortschritte in XYZ sind bemerkenswert, und wir freuen uns über deine kontinuierlichen Verbesserungen.'
            assistenVerbessert = assistenVerbessert.replace('XYZ', subject)
            messages.append({'role': 'user', 'content': userVerbessert})
            messages.append({'role': 'assistant', 'content': assistenVerbessert})

        if subject in faecherAndere:
            #print('Baue History mit Fach Andere: ' + subject)
            userKreativ = 'XYZ: kreativ'
            userKreativ = userKreativ.replace('XYZ', subject)
            assistenKreativ = 'Deine Kreativität kommt besonders im XYZunterricht zum Ausdruck. Du hast ein außergewöhnliches Talent und beeindruckst mit deinen originellen Ideen. .'
            assistenKreativ = assistenKreativ.replace('XYZ', subject)
            messages.append({'role': 'user', 'content': userKreativ})
            messages.append({'role': 'assistant', 'content': assistenKreativ})
            userAktiv = 'XYZ: aktiv'
            userAktiv = userAktiv.replace('XYZ', subject)
            assistenAktiv = 'Im XYZunterricht bist du sehr aktiv und beteiligst dich gerne an den Aktivitäten.'
            assistenAktiv = assistenAktiv.replace('XYZ', subject)
            messages.append({'role': 'user', 'content': userAktiv})
            messages.append({'role': 'assistant', 'content': assistenAktiv})

        userMotiviert = 'XYZ: motiviert'
        userMotiviert = userMotiviert.replace('XYZ', subject)
        assistenMotiviert = 'Im XYZunterricht bist du stets motiviert und gibst immer dein Bestes.'
        assistenMotiviert = assistenMotiviert.replace('XYZ', subject)
        messages.append({'role': 'user', 'content': userMotiviert})
        messages.append({'role': 'assistant', 'content': assistenMotiviert})

        if subject not in faecherNormal and subject not in faecherAndere:
            #print(f'Baue History für Softskills. Fach leer: {subject}.')
            userHilfsbereit = 'hilfsbereit'
            assistenHilfsbereit = 'Besonders schätzen wir deine Hilfsbereitschaft im Klassenzimmer. Du bist stets bereit, deinen Lehrer oder Mitschülern zu helfen, und trägst so zu einem positiven Lernklima bei.'
            messages.append({'role': 'user', 'content': userHilfsbereit})
            messages.append({'role': 'assistant', 'content': assistenHilfsbereit})
            userStill = 'still im unterricht'
            assistenStill = 'Obwohl du im Unterricht eher still bist, schätzen wir deine aufmerksame und konzentrierte Art. Du arbeitest stets fleißig mit und zeigst dabei große Ausdauer.'
            messages.append({'role': 'user', 'content': userStill})
            messages.append({'role': 'assistant', 'content': assistenStill})
            userTeamarbeit = 'teamfähig'
            assistenTeamarbeit = 'Besonders hervorheben möchten wir deine Fähigkeit zur Teamarbeit. Du arbeitest gut mit deinen Mitschülern zusammen und trägst aktiv zur Gruppenarbeit bei.'
            messages.append({'role': 'user', 'content': userTeamarbeit})
            messages.append({'role': 'assistant', 'content': assistenTeamarbeit})

        return messages
