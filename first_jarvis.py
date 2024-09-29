import os
import speech_recognition as sr
import pyttsx3


#creer mon moteur lié a pttsx3:

engine = pyttsx3.init('sapi5')

#je gere le volume et debit de la voix du robot:
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 220)

#je créé une liste avec toute les voix:
voix = engine.getProperty('voices')
#je prend celle que je veux et je la set:
engine.setProperty('voice', voix[0])




def speak(text):
    """Fonction qui fait parler le robot avec le text en argument"""
    engine.say(text)
    engine.runAndWait()


def take_command():
    '''     Fonction qui va:
              -écouter ma voix
              -la stocker dans 'queri
              -la return                  '''

    # je setup la prise de son:
    #je créé un objet 'reconnaisseur vocal':

    r = sr.Recognizer()
    #j'ouvre le micro et ce qui est input est dans 'source' ( mais n'est pas sauvergarder!):
    with sr.Microphone() as source:
        print('Listenning')
        #je determine un delai de pause // delai passé = fin d'ecoute:
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('recognize...')
            #je stock l'audio que je fait traduire dans queri:
            queri = r.recognize_google(audio, language='fr-FR')

            #je met un trigger pour quitter à la voix:
            if not 'au revoir' in queri:
                print(queri)

            else:
                speak('A la prochaine.')
                exit()


        except Exception:
            speak('je n\'ai pas comrpis...')
            queri = 'rien'

        return queri



if __name__=='__main__':

    while True:
        #je créé une varibale dans laquelle je stock la phrase que j'ai dite dans l'ordre.
        query = take_command().lower()

        #Maintenant je peux assigner plein d'odre en focnction de morceaux de string dans ma phrase oral:

        if 'ouvrir une page internet' in query:
            os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")

        #etc etc !!!!
