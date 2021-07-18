from os import listdir
from os.path import join as path_join
from subprocess import check_output

inDir=r'.\csv' #Directory holding input files
outDir=r'.\json' #Directory holding output files

#Change to whatever version your system is running, remove the folder if on Path
cycloneAddress=r'.\cyclonedx-win-x64'

files = listdir(inDir)
complete = 0

print("Beginning bulk csv conversion")
print(f"{len(files)} Files to Convert\n")

for each_file in files:
  filename,ext = each_file.split(".")
  args = [
      cycloneAddress,
      'convert',
      '--input-file', path_join(inDir, filename+"."+ext),
      '--output-file', path_join(outDir, filename+".json")
    ]
  try:
    check_output(args)
    print(f"Successfully Converted {filename}.{ext} to json!")
    complete += 1
  except:
    print(f"Something went wrong with converting {filename} to json!")

print(f"\n{complete} Successful conversions. {len(files)-complete} failures!")
