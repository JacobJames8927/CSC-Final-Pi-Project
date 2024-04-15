
const int trigPin = 13;
const int echoPin_1 = 12;
const int echoPin_2 = 10;

float duration_1, distance_1, duration_2, distance_2;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin_1, INPUT);
  pinMode(echoPin_2, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigPin, LOW);

  duration_1 = pulseIn(echoPin_1, HIGH);
  distance_1 = (duration_1*.0343)/2;

  duration_2 = pulseIn(echoPin_2, HIGH);
  distance_2 = (duration_1* .0343)/2
    
  Serial.print("Distance One: ");
  Serial.print(distance_1);
  Serial.print("Distance Two: ");
  Serialprint(distance_2);
  delay(100);
}
