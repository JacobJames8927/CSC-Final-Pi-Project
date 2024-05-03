const int trigPin_1 = 13;
const int trigPin_2 = 8;
const int echoPin_1 = 12;
const int echoPin_2 = 10;

int population = 0;

float duration_1, distance_1, duration_2, distance_2,past_distance_1, past_distance_2;

void setup() {
  pinMode(trigPin_1, OUTPUT);
  pinMode(trigPin_2, OUTPUT);
  pinMode(echoPin_1, INPUT);
  pinMode(echoPin_2, INPUT);
  Serial.begin(9600);
}

void loop() {
  
  digitalWrite(trigPin_1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_1, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigPin_1, LOW);

  duration_1 = pulseIn(echoPin_1, HIGH);
  distance_1 = (duration_1*.0343)/2;
  
  delay(50);
  
  digitalWrite(trigPin_2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_2, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigPin_2, LOW);

  duration_2 = pulseIn(echoPin_2, HIGH);
  distance_2 = (duration_2*.0343)/2;
    
  //Serial.print("Distance One: ");
  //Serial.println(distance_1);
  //Serial.print("Distance Two: ");
  //Serial.println(distance_2);
  Serial.println(population);

  check_for_human(distance_1, distance_2);
  past_distance_1 = distance_1;
  past_distance_2 = distance_2;
  delay(50);
}

float check_for_human(float distance_1, float distance_2) {
  if (distance_1 != past_distance_1 + 15 || distance_1 != past_distance_1 - 15){
    if (distance_1 <= 15){
      population += 1;
    }
    
  };
  if (distance_2 != past_distance_2 + 15 || distance_2 != past_distance_2 - 15){
    if (distance_2 <= 15){
      population += 1;
    }
  };
}
