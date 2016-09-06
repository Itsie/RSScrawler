# Vorbereitung

Installiere Python und alle ```requirements.txt```.

Installiere außerdem py2exe und Resourcehacker.

Quellcode herunterladen & entpacken.

# Dateien

```setup.py``` und ```RSScrawler.ico``` in Quellpfad verschieben.

```README.md``` und ```.gitignore``` löschen (optional).

# RSScrawler.py/Unicode Probleme beheben

```┌``` und ```┐``` durch ```.``` ersetzen.

```│``` und ```├``` und ```┤``` durch ```|``` ersetzen.

```└``` und ```┘``` durch ```'``` ersetzen.

```Ä``` durch Ae ersetzen.

```ä``` durch ae ersetzen.

```Ö``` durch Oe ersetzen.

```ö``` durch oe ersetzen.

```Ü``` durch Ue ersetzen.

```ü``` durch ue ersetzen.

# CMD

```cd Quellpfad```.

```python setup.py install```.

# Resource Hacker

Set all Resources to ```German/German```.

Replace Icon with ```setup.ico```.

Fix VersionInfo ```0x0409``` to ```0x0407```.
