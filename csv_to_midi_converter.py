import sys
import py_midicsv as pm
import os

def midi_to_csv(midi_file):
    csv_string_list = pm.midi_to_csv(midi_file)
    csv_file = os.path.splitext(midi_file)[0] + "_converted.csv"
    with open(csv_file, "w") as f:
        f.writelines(csv_string_list)
    print(f"Converted {midi_file} to {csv_file}")

def csv_to_midi(csv_file):
    with open(csv_file, "r") as f:
        csv_string_list = f.readlines()
    midi_object = pm.csv_to_midi(csv_string_list)
    midi_file = os.path.splitext(csv_file)[0] + "_converted.mid"
    with open(midi_file, "wb") as output_file:
        midi_writer = pm.FileWriter(output_file)
        midi_writer.write(midi_object)
    print(f"Converted {csv_file} to {midi_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_midi_converter.py [midi2csv|csv2midi] <input_file>")
        sys.exit(1)
    mode, input_file = sys.argv[1], sys.argv[2]
    if mode == "midi2csv":
        if input_file.endswith("midi"):
            midi_to_csv(input_file)
        else:
            print("Enter proper file type")
            sys.exit(3)
    elif mode == "csv2midi":
        if input_file.endswith("csv"):
            csv_to_midi(input_file)
        else:
            print("Enter proper file type")
            sys.exit(3)
    else:
        print("Unknown mode. Use 'midi2csv' or 'csv2midi'.")
        sys.exit(1)