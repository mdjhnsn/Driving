## Import Data
faces = read.csv("Files/data-faces.csv")
stimuli = read.csv("Files/data-stimuli.csv")

faces$Event.Switch = 0

## Join the datasets
for (i in 1:nrow(faces)) {
  
  x = stimuli[i, ]
  
  faces$Event.Switch[
    stimuli$ID == x$ID & 
      stimuli$Time >= x$StartTime & 
      stimuli$Time <= x$EndTime
    ] = 1
  
}