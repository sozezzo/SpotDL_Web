cls
md c:\temp\spotdl\
cls


docker run -d --name spot -p 3000:3000 -v /c/temp/spotdl:/app/downloads msozezzo/spotdl-web:spot-web


timeout 90

