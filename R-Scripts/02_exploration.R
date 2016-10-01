library(plyr)
library(reshape2)
library(ggplot2)

rm(list = ls())
load("R-Data/faces.rda")

## 8 Total Simulations, not all of the Subjects have data for every simulation

## What are the total frames by Sim per Subject?
dcast(ddply(faces, .(Subject, Trial), summarise, count = length(ID)), Subject ~ Trial)

## What are the crash events
ddply(faces, .(Event), summarise, count = length(ID))



x = subset(faces, Trial == '008')
x = melt(x, id.vars = c("Subject", "Age", "Gender", "Time", "Event"),
         measure.vars = c("Anger", "Contempt", "Disgust", "Fear", "Joy", 
                          "Sad", "Surprise", "Neutral"))

ggplot(subset(x, Subject == 'T001'), 
       aes(x = Time, y = value, group = Subject, color = Event)) +
  geom_point(alpha = .1) +
  geom_smooth(size = .2, se = FALSE)+
  facet_wrap(~variable)







x = subset(faces, Subject == 'T001')
x = melt(x, id.vars = c("Subject", "Trial", "Age", "Gender", "Time", "Event"),
         measure.vars = c("Anger", "Contempt", "Disgust", "Fear", "Joy", 
                          "Sad", "Surprise", "Neutral"))

ggplot(x, aes(x = Time, y = value, color = Event)) +
  geom_point(alpha = .05, size = .25) +
  facet_grid(Trial~variable) +
  scale_color_brewer(type = "qual", palette = 2) +
  guides(colour = guide_legend(override.aes = list(alpha = 1, size = 1)))




x = subset(faces.cen, Trial %in% c('004', '005', '006', '007') & Subject == 'T001')
x = melt(x, id.vars = c("Subject", "Trial", "Age", "Gender", "Time", "Event"),
         measure.vars = c("Anger", "Contempt", "Disgust", "Fear", "Joy", 
                          "Sad", "Surprise", "Neutral"))

ggplot(x, aes(x = Time, y = value, color = Event)) +
  geom_point(alpha = .05, size = .25) +
  facet_grid(Trial~variable) +
  scale_color_brewer(type = "qual", palette = 2) +
  guides(colour = guide_legend(override.aes = list(alpha = 1, size = 1)))
