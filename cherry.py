# -*- coding: utf-8 -*-
# RSScrawler - Version 2.0.7
# Projekt von https://github.com/rix1337

import cherrypy
import os, sys
import StringIO
from rssconfig import RssConfig
from RSScrawler import checkFiles

# Globale Variable
version = "v.2.0.7"

class Server:
  # Zeige Konfigurationsseite
  @cherrypy.expose
  def index(self):
    # importiere Einstellungen
    main = RssConfig('RSScrawler')
    jdownloader = main.get("jdownloader")
    port = main.get("port")
    prefix = main.get("prefix")
    interval = main.get("interval")
    hoster = main.get("hoster")
    pushbulletapi = main.get("pushbulletapi")
    # MB-Bereich
    mb = RssConfig('MB')
    mbquality = mb.get("quality")
    ignore = mb.get("ignore")
    historical = str(mb.get("historical"))
    crawl3d = str(mb.get("crawl3d"))
    enforcedl = str(mb.get("enforcedl"))
    crawlseasons = str(mb.get("crawlseasons"))
    seasonsquality = mb.get("seasonsquality")
    seasonssource = mb.get("seasonssource")
    # SJ-Bereich
    sj = RssConfig('SJ')
    sjquality = sj.get("quality")
    rejectlist = sj.get("rejectlist")
    regex = str(sj.get("regex"))
    # Erkenne Docker Umgebung
    if dockerglobal == '1':
      dockerblocker = ' disabled'
      dockerhint = 'Docker-Modus: Kann nur per Docker-Run angepasst werden! '
    else:
      dockerblocker = ''
      dockerhint = ''
    return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" action="https://github.com/rix1337/thanks">
          <img src="data:image/png;base64,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" alt=""/>
          <h1>RSScrawler</h1>
          ''' + version + ''' (Projekt von <a target="_parent" href="https://github.com/rix1337/RSScrawler/commits">RiX</a>)
          <button type="submit">Bedanken</button>
    </form>
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="logleeren?wert=1">
          <h1>Log</h1>
            <iframe src="./log" width="100%" height="200" frameborder="1">
            Dieser Browser unterstützt keine iFrames. Stattdessen <a target="_parent" href = "/log">/log</a> aufrufen.
          </iframe>
          <button type="submit">Leeren</button>
    </form>
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="speichern">
          <div hinweis="Hier werden sämtliche Einstellungen von RSScrawler hinterlegt.Dieses Script funktioniert nur sinnvoll, wenn Ordnerüberwachung im JDownloader aktiviert ist.Es muss weiterhin unten der richtige JDownloader Pfad gesetzt werden!"><h1>Einstellungen</h1></div>
          <div hinweis="Diese allgemeinen Einstellungen müssen korrekt sein"><h3>Allgemein</div>
          Pfad des JDownloaders:<div hinweis="''' + dockerhint +'''Dieser Pfad muss das exakte Verzeichnis des JDownloaders sein, sonst funktioniert das Script nicht!"><input type="text" value="''' + jdownloader +'''" name="jdownloader"''' + dockerblocker +'''></div>
          Port:<div hinweis="''' + dockerhint +'''Hier den Port des Webservers für Einstellungen und Log wählen"><input type="text" name="port" value="''' + port +'''"''' + dockerblocker +'''></div>
          Prefix:<div hinweis="Hier den Prefx des Webservers für Einstellungen und Log wählen. Nützlich für Proxys"><input type="text" name="prefix" value="''' + prefix +'''"></div>
          Suchintervall:<div hinweis="Das Suchintervall in Minuten sollte nicht zu niedrig angesetzt werden um keinen Ban zu riskieren"><input type="text" name="interval" value="''' + interval +'''"></div>
          Pushbullet API-Schlüssel:<div hinweis="Um über hinzugefügte Releases informiert zu werden hier den Pushbullet API-Key eintragen"><input type="text" name="pushbulletapi" value="''' + pushbulletapi +'''"></div>
          Hoster:<div hinweis="Hier den gewünschten Hoster eintragen (Uploaded oder Share-Online). Möglich sind auch beide (durch Kommata getrennt)"><input type="text" name="hoster" value="''' + hoster +'''"></div>
          <div hinweis="Dieser Bereich ist für die Suche auf Movie-Blog.org zuständig"><h3>Movie-Blog</h3></div>
          Auflösung:<div hinweis="Die Qualität, nach der Gesucht wird (1080p, 720p oder 480p)"><input type="text" name="mbquality" value="''' + mbquality +'''"></div>
          Filterliste:<div hinweis="Releases mit diesen Begriffen werden nicht hinzugefügt (durch Kommata getrennt)"><input type="text" name="ignore" value="''' + ignore +'''"></div>
          Suchfunktion statt Feed nutzen:<div hinweis="Wenn aktiviert wird die MB-Suchfunktion genutzt (langsamer), da der Feed nur wenige Stunden abbildet"><input type="text" name="historical" value="''' + historical +'''"></div>
          3D-Releases suchen:<div hinweis="Wenn aktiviert sucht das Script nach 3D Releases (in 1080p), unabhängig von der oben gesetzten Qualität"><input type="text" name="crawl3d" value="''' + crawl3d +'''"></div>
          Zweisprachige Releases suchen:<div hinweis="Wenn aktiviert sucht das Script zu jedem nicht-zweisprachigen Release (kein DL-Tag im Titel) ein passendes Release in 1080p mit DL Tag. Findet das Script kein Release wird dies im Log vermerkt. Bei der nächsten Ausführung versucht das Script dann erneut ein passendes Release zu finden. Diese Funktion ist nützlich um (durch späteres Remuxen) eine zweisprachige Bibliothek in 720p zu halten."><input type="text" name="enforcedl" value="''' + enforcedl +'''"><br /></div>
          Staffeln suchen:<div hinweis="Komplette Staffeln von Serien landen zuverlässiger auf MB als auf SJ. Diese Option erlaubt die entsprechende Suche"><input type="text" name="crawlseasons" value="''' + crawlseasons +'''" ></div>
          Auflösung der Staffeln:<div hinweis="Die Qualität, nach der Staffeln gesucht werden (1080p, 720p oder 480p)"><input type="text" name="seasonsquality" value="''' + seasonsquality +'''"></div>
          Quellart der Staffeln:<div hinweis="Der Staffel-Releasetyp nach dem gesucht wird"><input type="text" name="seasonssource" value="''' + seasonssource +'''"></div>
          <div hinweis="Dieser Bereich ist für die Suche auf Serienjunkies.org zuständig"><h3>SerienJunkies</h1></div>
          <p>Auflösung:<div hinweis="Die Qualität, nach der Gesucht wird (1080p, 720p oder 480p)"><input type="text" name="sjquality" value="''' + sjquality +'''"></div>
          Filterliste:<div hinweis="Releases mit diesen Begriffen werden nicht hinzugefügt (durch Kommata getrennt)"><input type="text" name="rejectlist" value="''' + rejectlist +'''"></div>
          Auch per RegEx-Funktion suchen:<div hinweis="Wenn aktiviert werden in einer zweiten Suchdatei Serien nach Regex-Regeln gesucht"><input type="text" name="regex" value="''' + regex +'''"></div>
          <button type="submit">Speichern</button>
    </form>
    <form id="rsscrawler" action="https://www.9kw.eu/register_87296.html">
          <h1>Captchas</h1>
          <button type="submit">Captchas automatisch lösen lassen</button>
    </form>
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="listenspeichern">
          <h1>Suchlisten</h1>
          <div hinweis="Pro Zeile ein Filmtitel"><h3>Filme</h3></div>
          <textarea name="mbfilme">''' + self.getListe('MB_Filme') + '''</textarea>
          <div hinweis="Pro Zeile ein Serientitel für ganze Staffeln"><h3>Staffeln</h3></div>
          <textarea name="mbstaffeln">''' + self.getListe('MB_Staffeln') + '''</textarea>
          <div hinweis="Pro Zeile ein Serientitel"><h3>Serien</h3></div>
          <textarea name="sjserien">''' + self.getListe('SJ_Serien') + '''</textarea>
          <div hinweis="Pro Zeile ein Serientitel im RegEx-Format. Filter werden ignoriert! DEUTSCH.*Serien.Titel.*.S01.*.720p.*-GROUP sucht nach Releases der Gruppe GROUP von Staffel 1 der Serien Titel in 720p auf Deutsch. Serien.Titel.* sucht nach allen Releases von Serien Titel (nützlich, wenn man sonst HDTV aussortiert). Serien.Titel.*.DL.*.720p.* sucht nach zweisprachigen Releases in 720p von Serien Titel. ENGLISCH.*Serien.Titel.*.1080p.* sucht nach englischen Releases in Full-HD von Serien Titel. (?!(Diese|Andere)).*Serie.*.DL.*.720p.*-(GROUP|ANDEREGROUP) sucht nach Serie (aber nicht Diese Serie oder Andere Serie), zweisprachig und in 720p und ausschließlich nach Releases von GROUP oder ANDEREGROUP."><h3>Serien (RegEx)</h3></div>
          <textarea name="sjregex">''' + self.getListe('SJ_Serien_Regex') + '''</textarea>
          <button type="submit">Speichern</button>
    </form>
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="neustart?wert=1">
          <button type="submit">Neu starten</button>
    </form>
  </div>
  </body>
</html>'''

  # /log zeigt den Inhalt des RSScrawler.log
  @cherrypy.expose
  def log(self):
    # Wenn Log (noch) nicht vorhanden, Zeige Meldung
    if not os.path.isfile(os.path.join(os.path.dirname(sys.argv[0]), 'RSScrawler.log')):
      return "Kein Log vorhanden!"
    else:
      # Deklariere Pfad der Logdatei (relativ)
      logfile = open(os.path.join(os.path.dirname(sys.argv[0]), 'RSScrawler.log'))
      # Nutze String um Log in HTML anzuzeigen
      output = StringIO.StringIO()
      #Füge Meta-Tag hinzu, damit Log regelmäßig neu geladen wird
      output.write("<meta http-equiv='refresh' content='30'>")
      # Jede Zeile der RSScrawler.log wird eingelesen. Letzter Eintrag zuerst, zwecks Übersicht
      for lines in reversed(logfile.readlines()):
        # Der Newline-Charakter \n wird um den HTML Newline-Tag <br> ergänzt
        output.write(lines.replace("\n", "<br>\n"))
      return output.getvalue()

  @cherrypy.expose
  def speichern(self, jdownloader, port, prefix, interval, pushbulletapi, hoster, mbquality, ignore, historical, crawl3d, enforcedl, crawlseasons, seasonsquality, seasonssource, sjquality, rejectlist, regex):
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/RSScrawler.ini'), 'wb') as f:
      # RSScrawler Section:
      f.write('# RSScrawler.ini (Stand: RSScrawler ' + version + ')\n')
      f.write("\n[RSScrawler]\n")
      f.write("jdownloader = " + jdownloader.encode('utf-8') + "\n")
      f.write("port = " + port + "\n")
      f.write("prefix = " + prefix.encode('utf-8') + "\n")
      f.write("interval = " + interval.encode('utf-8') + "\n")
      f.write("pushbulletapi = " + pushbulletapi.encode('utf-8') + "\n")
      f.write("hoster = " + hoster.encode('utf-8') + "\n")
      # MB Section:
      f.write("\n[MB]\n")
      f.write("quality = " + mbquality.encode('utf-8') + "\n")
      f.write("ignore = " + ignore.encode('utf-8') + "\n")
      f.write("historical = " + historical.encode('utf-8') + "\n")
      f.write("crawl3d = " + crawl3d.encode('utf-8') + "\n")
      f.write("enforcedl = " + enforcedl.encode('utf-8') + "\n")
      f.write("crawlseasons = " + crawlseasons.encode('utf-8') + "\n")
      f.write("seasonsquality = " + seasonsquality.encode('utf-8') + "\n")
      f.write("seasonssource = " + seasonssource.encode('utf-8') + "\n")
      # SJ Section:
      f.write("\n[SJ]\n")
      f.write("quality = " + sjquality.encode('utf-8') + "\n")
      f.write("rejectlist = " + rejectlist.encode('utf-8') + "\n")
      f.write("regex = " + regex.encode('utf-8') + "\n")
      checkFiles()
      return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="../''' + prefix.encode('utf-8') + '''">
          <h1>Gespeichert!</h1>
          Die Einstellungen wurden gespeichert.
          <button type="submit">Zurück</button>
    </form>
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="neustart?wert=1">
          <h1>Hinweis</h1>
          Um einige Änderungen anzunehmen muss RSScrawler neu gestartet werden!
          <button type="submit">Neu starten</button>
    </form>
  </div>
  </body>
</html>'''

  @cherrypy.expose
  def listenspeichern(self, mbfilme, mbstaffeln, sjserien, sjregex):
    main = RssConfig('RSScrawler')
    prefix = main.get("prefix")
    if mbfilme == '':
      mbfilme = 'Ein Titel Pro Zeile - BEACHTE DIE HINWEISE'
    if mbstaffeln == '':
      mbstaffeln = 'Ein Titel Pro Zeile - BEACHTE DIE HINWEISE'
    if sjserien == '':
      sjserien = 'Ein Titel Pro Zeile - BEACHTE DIE HINWEISE'
    if sjregex == '':
      sjregex = 'Ein Titel Pro Zeile - BEACHTE DAS REGEX FORMAT UND DIE HINWEISE'
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Listen/MB_Filme.txt'), 'wb') as f:
      f.write(mbfilme.encode('utf-8'))
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Listen/MB_Staffeln.txt'), 'wb') as f:
      f.write(mbstaffeln.encode('utf-8'))
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Listen/SJ_Serien.txt'), 'wb') as f:
      f.write(sjserien.encode('utf-8'))
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Listen/SJ_Serien_Regex.txt'), 'wb') as f:
      f.write(sjregex.encode('utf-8'))
    checkFiles()
    return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="../''' + prefix.encode('utf-8') + '''">
          <h1>Gespeichert!</h1>
          <button type="submit">Zurück</button>
    </form>
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="neustart?wert=1">
          <h1>Hinweis</h1>
          Um direkt nach den neuen Listeneinträgen zu suchen muss neu gestartet werden
          <button type="submit">Neu starten</button>
    </form>
  </div>
  </body>
</html>'''

  @cherrypy.expose
  def logleeren(self, wert):
    main = RssConfig('RSScrawler')
    prefix = main.get("prefix")
    open(os.path.join(os.path.dirname(sys.argv[0]), 'RSScrawler.log'), 'w').close()
    if wert == '1':
      return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="../''' + prefix.encode('utf-8') + '''">
          <h1>Log geleert!</h1>
          <button type="submit">Zurück</button>
    </form>
  </div>
  </body>
</html>'''
    else:
      return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="../''' + prefix.encode('utf-8') + '''">
          <h1>Log nicht geleert! Bestätigungscode fehlt.</h1>
          <button type="submit">Zurück</button>
    </form>
  </div>
  </body>
</html>'''
      
  @cherrypy.expose
  def neustart(self, wert):
    main = RssConfig('RSScrawler')
    prefix = main.get("prefix")
    if wert == '1':
      os.execl(sys.executable, sys.executable, *sys.argv)
      return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="../''' + prefix.encode('utf-8') + '''">
          <h1>Neustart ausgeführt!</h1>
          <button type="submit">Zurück</button>
    </form>
  </div>
  </body>
</html>'''
    else:
      return '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width,maximum-scale=1" name="viewport">
    <meta content="noindex, nofollow" name="robots">
    <title>RSScrawler</title>
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAwUExURUxpcQEBAQMDAwAAAAAAAAICAgAAAAAAAAAAAAEBAQQEBAEBAQMDAwEBAQICAgAAAHF9S8wAAAAPdFJOUwBkHuP2K8qzcEYVmzhVineWhWQAAAB4SURBVAjXY2CAAaabChAG4xdzIQjj//9vAiAGZ7L/f+8FINai2fb/q4A0z1uF4/9/g9XYae3/IgBWnLr8fxIDA2u7/zcd+x9AuTXC/x/s/76AgSml0N90yucABt7/nvUfF3+ZwMBqn9T/j+0/UNvBgIhO3o4AuCsAPDssr9goPWoAAABXelRYdFJhdyBwcm9maWxlIHR5cGUgaXB0YwAAeJzj8gwIcVYoKMpPy8xJ5VIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4A6hcRdPJCNZUAAAAASUVORK5CYII=", rel="icon" type="image/png">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);.copyright,[hinweis]:before,div,h1,h2,h3,input{text-align:center}*{margin:0;padding:0;box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-webkit-font-smoothing:antialiased;-moz-font-smoothing:antialiased;-o-font-smoothing:antialiased;font-smoothing:antialiased;text-rendering:optimizeLegibility}body{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:100;font-size:14px;line-height:30px;color:#000;background:#d3d3d3}.container{max-width:800px;width:100%;margin:0 auto;position:relative}[hinweis]:after,[hinweis]:before{position:absolute;bottom:150%;left:50%}#rsscrawler button[type=submit],#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{font:400 12px/16px Roboto,Helvetica,Arial,sans-serif}#rsscrawler{background:#F9F9F9;padding:25px;margin:50px 0;box-shadow:0 0 20px 0 rgba(0,0,0,.2),0 5px 5px 0 rgba(0,0,0,.24)}#rsscrawler h1{display:block;font-size:30px;font-weight:300;margin-bottom:10px}#rsscrawler h4{margin:5px 0 15px;display:block;font-size:13px;font-weight:400}fieldset{border:none!important;margin:0 0 10px;min-width:100%;padding:0;width:100%}#rsscrawler iframe,#rsscrawler input[type=text],#rsscrawler textarea{width:100%;border:1px solid #ccc;background:#FFF;margin:0 0 5px;padding:10px}#rsscrawler iframe,#rsscrawler input[type=text]:hover,#rsscrawler textarea:hover{-webkit-transition:border-color .3s ease-in-out;-moz-transition:border-color .3s ease-in-out;transition:border-color .3s ease-in-out;border:1px solid #aaa}#rsscrawler textarea{height:100px;max-width:100%;resize:none}#rsscrawler button[type=submit]{cursor:pointer;width:100%;border:none;background:#333;color:#FFF;margin:0 0 5px;padding:10px;font-size:15px}#rsscrawler button[type=submit]:hover{background:#43A047;-webkit-transition:background .3s ease-in-out;-moz-transition:background .3s ease-in-out;transition:background-color .3s ease-in-out}#rsscrawler button[type=submit]:active{box-shadow:inset 0 1px 3px rgba(0,0,0,.5)}#rsscrawler input:focus,#rsscrawler textarea:focus{outline:0;border:1px solid #aaa}::-webkit-input-placeholder{color:#888}:-moz-placeholder{color:#888}::-moz-placeholder{color:#888}:-ms-input-placeholder{color:#888}[hinweis]{position:relative;z-index:2;cursor:pointer}[hinweis]:after,[hinweis]:before{visibility:hidden;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=0);opacity:0;pointer-events:none}[hinweis]:before{margin-bottom:5px;margin-left:-400px;padding:9px;width:782px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:0;background-color:#000;background-color:hsla(0,0%,20%,.9);color:#fff;content:attr(hinweis);font-size:14px;line-height:1.2}[hinweis]:after{margin-left:-5px;width:0;border-top:5px solid #000;border-top:5px solid hsla(0,0%,20%,.9);border-right:5px solid transparent;border-left:5px solid transparent;content:" ";font-size:0;line-height:0}[hinweis]:hover:after,[hinweis]:hover:before{visibility:visible;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";filter:progid: DXImageTransform.Microsoft.Alpha(Opacity=100);opacity:1}
    </style>
  </head>
  <body>
  <div class="container">
    <form id="rsscrawler" enctype="multipart/form-data" method="post" action="../''' + prefix.encode('utf-8') + '''">
          <h1>Neustart nicht ausgeführt! Bestätigungscode fehlt.</h1>
          <button type="submit">Zurück</button>
    </form>
  </div>
  </body>
</html>'''
      
  def getListe(self, liste):
    if not os.path.isfile(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Listen/' + liste + '.txt')):
      return "Liste nicht gefunden"
    else:
      file = open(os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Listen/' + liste + '.txt'))
      output = StringIO.StringIO()
      for line in file.readlines():
        output.write(line)
      return output.getvalue()

  @classmethod
  def run(cls, prefix):
    cherrypy.quickstart(cls(), '/' + prefix, os.path.join(os.path.dirname(sys.argv[0]), 'Einstellungen/Web/cherry.conf'))
    
  def start(self, port, prefix, docker):
    # Setzte Variable um Docker-Umgebung zu erkennen
    global dockerglobal
    dockerglobal = docker
    # Deaktiviere Cherrypy Log
    cherrypy.log.error_log.propagate = False
    cherrypy.log.access_log.propagate = False
    # Setze das Port entsprechend des Aufrufs
    cherrypy.config.update({'server.socket_port': port})
    # Setzte den Pfad der Webanwendung entsprechend des Aufrufs
    self.run(prefix)