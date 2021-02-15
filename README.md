pip install webssh

Then move into the cloned repo

Run from cmd prompt :

  python manage.py runserver


IMPORTANT:
  
  Edit in myexam/view.py
    
    def Split....
    
      os.system("wssh --fbidhttp=False")

