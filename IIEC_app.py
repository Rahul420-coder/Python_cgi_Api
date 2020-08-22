import pyttsx3
import os

pyttsx3.speak("hey... Rahul Rathod. i'm Your System. and how are you? I think your not fine. ok. Tell me. ")

while True:

	pyttsx3.speak(" What i do for you ")
	print("hey... What i do for you :)  " , end="")
	text = input()

	if (("open" in text) or ("run" in text)) and (("Chrome" in text) or ("chrome" in text)):
		pyttsx3.speak("Chrome Browser is Successfully open.")
		os.system("chrome")
		pyttsx3.speak("Chrome Browser is Closed.")
		print("\n===========================================================================================\n\n\n                        Chrome Browser was Successfully opened.                           \n\n\n===========================================================================================\n" )
		
	elif (("run" in  text) or ("open" in text)) and (("notepad" in text) or ("texteditor" in text)):
		pyttsx3.speak("Notepad TextEditor is Successfully open.")
		os.system("notepad")
		pyttsx3.speak("Notepad TextEditor is Closed.")
		print("\n===========================================================================================\n\n\n                      Notepad TextEditor was Successfully opened.                           \n\n===========================================================================================\n" )
	
	elif (("open" in text) or ("run" in text)) and (("vlc" in text) or ("video" in text)):
		pyttsx3.speak("VLC Media Player is Successfully open.")
		os.system("vlc")
		pyttsx3.speak("VLC Media Player is Closed.")
		print("\n===========================================================================================\n\n\n                      VLC Video Player was Successfully opened.                           \n\n\n===========================================================================================\n" )

	elif (("open" in text) or ("run" in text)) and (("control" in text) or ("panel" in text) or ("controlpanel" in text)):
		pyttsx3.speak("Control Panel is Successfully open.")
		os.system("control")
		pyttsx3.speak("Control Panel is Closed.")
		print("\n===========================================================================================\n\n\n                        Contrl Panel was Successfully opened.                           \n\n\n===========================================================================================\n" )
	
	elif ("python" in text) and (("-v" in text) or ("version" in text)):
		pyttsx3.speak("Python Version is Python 3.8.5.")
		print("\n===========================================================================================\n\n\n                      Python Version is Python 3.8.5.                           \n\n\n===========================================================================================\n" )

	elif (("exit" in text) or ("quit" in text)):
		pyttsx3.speak("Have a Nice day Sir . Now i think Your fine :)")
		print("\n===========================================================================================\n\n\n                          Have a nice day Sir.. okey Bye :)                            \n\n\n===========================================================================================\n" )
		break

	else:
		pyttsx3.speak("Your Enter Wrong text. so please Enter valid text.")
		print("\n===========================================================================================\n\n\n                            Your Enter Wrong Text :(                            \n\n\n===========================================================================================\n")