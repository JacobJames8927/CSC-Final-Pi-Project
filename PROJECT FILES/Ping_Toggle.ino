#include <EEPROM.h>


const int trigPin_1 = 13;
const int trigPin_2 = 8;
const int echoPin_1 = 12;
const int echoPin_2 = 10;
const int reset = 3;

int population = 0, detect_value = 15;

float duration_1, distance_1, duration_2, distance_2,past_distance_1, past_distance_2;

bool toggle_1, toggle_2;

void setup() {
  pinMode(trigPin_1, OUTPUT);
  pinMode(trigPin_2, OUTPUT);
  pinMode(echoPin_1, INPUT);
  pinMode(echoPin_2, INPUT);
  pinMode(reset, INPUT);
  Serial.begin(9600);
  get_data();
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
  if (distance_2 > detect_value){
      toggle_2 = 0;
    }
  if (distance_1 > detect_value){
    toggle_1 = 0;
  }
  delay(50);

  EEPROM.put(0, population);
  if (digitalRead(3) == HIGH){
    population = 0;
  }
  
}

float get_data(){
  population = EEPROM.get(0, population);
}

float check_for_human(float distance_1, float distance_2) {
  if (toggle_1 == 0){
    if (distance_1 <= detect_value){
      population += 1;
      toggle_1 = 1;
      
    
    }
    
  };
  if (toggle_2 == 0){
    if (distance_2 <= detect_value){
      population += 1;
      toggle_2 = 1;
      
    }
    
  }
}
