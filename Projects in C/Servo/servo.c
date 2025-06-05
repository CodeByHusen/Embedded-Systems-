#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

#define ServoPin    1  // define the servo to GPIO1

long Map(long value, long fromLow, long fromHigh, long toLow, long toHigh) {
    return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow;
}

void setAngle(int pin, int angle) {
    if (angle < 0)
        angle = 0;
    if (angle > 180)
        angle = 180;
    softPwmWrite(pin, Map(angle, 0, 180, 5, 25));
}

int main(void) {
    int i;
    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed!\n");
        return 1;
    }

    softPwmCreate(ServoPin, 0, 200);  // initialize PWM pin of servo

    while (1) {
        for (i = 0; i <= 180; i++) {
            setAngle(ServoPin, i);
            delay(20);  // etwas mehr Zeit für besseren Servo-Lauf
        }
        delay(1000);
        for (i = 180; i >= 0; i--) {
            setAngle(ServoPin, i);
            delay(20);
        }
        delay(1000);
    }
    return 0;
}
