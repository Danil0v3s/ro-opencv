opencv_traincascade -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 50 -numNeg 1000 -numStages 12 -maxFalseAlarmRate 0.4 -minHitRate 0.999 -precalcIdxBufSize 6000 -precalcValBufSize 6000 

 opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec