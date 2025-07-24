# Deakin Data Science Club: MIDI Time Series ML Demo

Welcome to the Deakin Data Science Club's MIDI Time Series Machine Learning Demo!  
This project is part of our Activations Showcase, designed to demonstrate the power of machine learning in a creative, musical context.

## Project Overview

The goal of this project is to show how machine learning can be applied to time series data—in this case, MIDI note sequences. We'll take live MIDI input from an audience member (using an MPC One or a DAW), convert the MIDI data to a CSV format, analyze and forecast the note sequences using machine learning, and then convert the results back to MIDI for playback.

## Workflow

1. **MIDI Input:**  
   An audience member plays a melody or rhythm on the MPC One or in a DAW.

2. **MIDI to CSV Conversion:**  
   The MIDI file is converted to a CSV file using our Python script (`csv_to_midi_converter.py`). This makes the note data easy to analyze and manipulate.

3. **Machine Learning Time Series Analysis:**  
   We apply machine learning models to the CSV data to forecast or generate new note sequences. This is where the "magic" happens—showing how ML can learn patterns and make predictions.

4. **CSV to MIDI Conversion:**  
   The (possibly modified or forecasted) CSV file is converted back to a MIDI file.

5. **Playback:**  
   The new MIDI file is loaded back into the DAW or MPC One for playback, letting everyone hear the results of the machine learning process.

## Project Goals

- **Demonstrate** how machine learning can be used for creative applications.
- **Engage** the audience with a live, interactive demo.
- **Educate** club members and attendees about time series analysis and MIDI data processing.
- **Showcase** the technical and creative skills of the Deakin Data Science Club.

## Getting Started

1. Clone this repository.
2. Make sure you have [Python](https://www.python.org/) installed.
3. Install the required Python package using pip:
   ```
   pip install py_midicsv
   ```
4. Use `csv_to_midi_converter.py` to convert between MIDI and CSV formats.
5. Explore the machine learning notebooks and scripts to analyze and forecast MIDI note sequences.

## Contributing

All club members are welcome to contribute!  
Please add your ideas, code, or improvements as we build out the demo.

---

*Let's make some music with machine