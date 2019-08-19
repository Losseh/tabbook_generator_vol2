# tabbook_generator_vol2

**FILES:**

*lists* - directory containing songs lists to be generated

*generate.sh* - main processor of tabs into PDF format. Definition of which lists will be generated (to separate PDF files) is located within the file, so don't be afraid when only one list gets generated. Probably solely this list is defined as the input to be generated. To generate them all, simply uncomment the line containing more lists.

*transform.py* - util script to transform standard [upper chords]+[lower text] format into [text left]+[chords right] in TEX format ("ly" file). This mechanism is able to process these "ly"s into beautiful PDF songbooks. 

**GUI?**
- opcje do wyboru:
  - spis treści on/off
  - taby/bez tabów
  - wybór piosenek
  - nierozrywalne bloki tekstu
