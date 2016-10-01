library(vars)
library(TTR)
library(astsa)
library(nnet)

rm(list = ls())
load("R-Data/faces.rda")


x = dcast(ddply(stats, .(Gender, Age, Trial, Event), summarise, count = length(Subject)), 
      Gender + Age + Event ~ Trial)
x[is.na(x)] = 0


x = subset(faces, ID == 'T003-007')

mdl = nnet(factor(Texting) ~ . - ID - Subject - Trial - Age - Gender - Frame - 
             Event.Switch - Texting - Event - Time, 
           data = x, size = 1)

x$pred = as.numeric(predict(mdl, x, type = "class"))
table(x$Texting, x$pred)

y = subset(faces, ID == 'T004-007')
y$pred = as.numeric(predict(mdl, y, type = "class"))
table(y$Texting, y$pred)

y2 = subset(faces, ID == 'T005-007')
y2$pred = as.numeric(predict(mdl, y2, type = "class"))
table(y2$Texting, y2$pred)


library(e1071)

mdl = svm(Texting ~ . - ID - Subject - Trial - Age - Gender - Frame - Time - Event.Switch - 
            Texting - Event, data = x)





