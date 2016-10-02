library(plyr)
library(reshape2)
library(ggplot2)

rm(list = ls())
load("R-Data/faces.rda")

## Calculate the baseline
baseline = ddply(subset(faces, Trial == '001'), 
                 .(Subject, Age, Gender), summarise,
                 mu_Anger = mean(Anger),
                 mu_Contempt = mean(Contempt),
                 mu_Disgust = mean(Disgust),
                 mu_Fear = mean(Fear),
                 mu_Joy = mean(Joy),
                 mu_Sad = mean(Sad),
                 mu_Surprise = mean(Surprise),
                 mu_Neutral = mean(Neutral))

faces.cen = faces
faces.cen = join(faces.cen, baseline, by = "Subject", type = "inner")

## Center all emotions
faces.cen$Anger = with(faces.cen, Anger - mu_Anger) * 100
faces.cen$Contempt = with(faces.cen, Contempt - mu_Contempt) * 100
faces.cen$Disgust = with(faces.cen, Disgust - mu_Disgust) * 100
faces.cen$Fear = with(faces.cen, Fear - mu_Fear) * 100
faces.cen$Joy = with(faces.cen, Joy - mu_Joy) * 100
faces.cen$Sad = with(faces.cen, Sad - mu_Sad) * 100
faces.cen$Surprise = with(faces.cen, Surprise - mu_Surprise) * 100
faces.cen$Neutral = with(faces.cen, Neutral - mu_Neutral) * 100

faces.cen = faces.cen[, -(19:28)]

## Calculate the average value and variance for each trial, event, expression
stats = ddply(faces.cen, .(Subject, Trial, Event, Age, Gender, Event.Switch), summarise,
               mu_Anger = mean(Anger),
               var_Anger = var(Anger),
               mu_Contempt = mean(Contempt),
               var_Contempt = var(Contempt),
               mu_Disgust = mean(Disgust),
               var_Disgust = var(Disgust),
               mu_Fear = mean(Fear),
               var_Fear = var(Fear),
               mu_Joy = mean(Joy),
               var_Joy = var(Joy),
               mu_Sad = mean(Sad),
               var_Sad = var(Sad),
               mu_Surprise = mean(Surprise),
               var_Surprise = var(Surprise),
               mu_Neutral = mean(Neutral),
               var_Neutral = var(Neutral))

stats[, 7:22] = apply(stats[, 7:22], 2, function(x) round(x, 3))

faces$Texting = 0
faces$Texting[faces$Event %in% c("Texting", "Texting and Talking")] = 1
faces$Texting = factor(faces$Texting)

save(list = c("stats", "faces", "baseline", "faces.cen"), file = "R-Data/faces.rda")
















