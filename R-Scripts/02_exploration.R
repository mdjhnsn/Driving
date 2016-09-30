library(plyr)
library(reshape2)
library(ggplot2)

## 8 Total Simulations, not all of the Subjects have data for every simulation

## What are the total frames by Sim per Subject?
dcast(ddply(faces, .(Subject, Trial), summarise, count = length(ID)), Subject ~ Trial)

## What are the crash events
ddply(faces, .(Event), summarise, count = length(ID))



x = subset(faces, Subject == 'T001')
x = melt(x[, c(3, 6, 9, 10:17)], id.vars = c("Trial", "Event", "Frame"))

ggplot(x) + 
  geom_point(aes(x = Frame, y = value, color = variable), alpha = .05) +
  facet_grid(Trial~Event)

library(astsa)
library(vars)

x = subset(faces, Subject == 'T001' & Trial == '007')

mdl = VAR(y = x[, 10:17], exogen = x[, 8])
