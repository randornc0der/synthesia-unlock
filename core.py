import os, sys, subprocess
import pymsgbox

from utils import appfolder, listr

def check():
    if os.path.exists(appfolder):
        print("Synthesia Found")
        print(os.getenv("APPDATA"))
        listr.append(f"{os.getenv('APPDATA')}")
    else:
        pymsgbox.alert("Error: Make Sure Synthesia Is Installed!")
        sys.exit(0)

def inject():
    try:
        result_del = subprocess.run(
            f'del /f /q "{appfolder}\\log.txt" "{appfolder}\\news.json" "{appfolder}\\settings.db" "{appfolder}\\settings.xml"',
            shell=True, check=True, capture_output=True, text=True
        )
        print("Delete output:", result_del.stdout)

        result_create = subprocess.run(
            f'echo ^<?xml version="1.0"?^>^<Settings version="1"^>^<setting key="Graphics.MonitorRectangle"^>0,0,1920,983^</setting^>^<setting key="Internet.LastMetadataCheck"^>16483^</setting^>^<setting key="Library.LastGroupPath"^>Keyboard Classics^</setting^>^<setting key="System.LastScreen"^>title^</setting^>^<setting key="System.Random"^>be7f5194-2f12-4478-9846-80428fb06554^</setting^>^<setting key="System.TutorialPresented"^>1^</setting^>^<setting key="System.UnlockKey"^>Synthkeysia77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxrIHY9IjEiIGk9IjQyMzQ2YTI5YWNlZTQxZmNhY2QwYjczZTBjZjNhZjVmIiB0PSJwIiBjPSIxIiB5PSIyMDA5IiBtPSIxMSIgZD0iNyIgbj0iQnJlbmRhbiBSb3NzbyIgcz0iZmNjMDlpZmEzNW5yOGlJb2pwalpVazdmRWx4cjViZCtxWHIzN0d0SzZBUXpmSUxRTktZK3IrUTJGajBZc3F0K1RQMnpwRmx6bjEwNXVrVHNNNDM3UmpPemRsUDV2a2ovZHhMNGY3VDYybWVJMk1NVDJma2MrRlhIaTcxaGNKN3hLUHdwQjc1STdVajlReGVIVURzcmRUemlrOXo3NWVSZlgrckNGcHI3SEdvPSIgLz4=aisyekhtnyS^</setting^>^</Settings^> > "{appfolder}\\settings.xml"',
            shell=True, check=True, capture_output=True, text=True
        )

        pymsgbox.alert("Unlock successful!", "Done")

    except subprocess.CalledProcessError as e:
        pymsgbox.alert(
            f"Command failed (code {e.returncode}):\n{e.stderr}",
            "Command Error"
        )
    except Exception as e:
        pymsgbox.alert(f"Unexpected error:\n{str(e)}", "Error")

def getit():
    from ui import win
    print(win.geometry())