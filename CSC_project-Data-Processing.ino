

//====Global Variables=====

//sensors: changes to 1 if person moves through. changes to 0 when both equal one.
//         order (in out, out in) determines if +/-.

//sensor group 1
int Person_in_1 = 0;
int Person_out_1 = 0;

//sensor group 2
int Person_in_2 = 0;
int Person_out_2 = 0;

//sensor group 3
int Person_in_3 = 0;
int Person_out_3 = 0;

//Population
int estimated_population = 0;

void setup() {



}


void loop() {
sensor_check(estimated_population);

}

//Note: need to change, once detects in/out, wait for change, then execute after. rn groups of people would be missed.
//can rework to take in a number from pressure plates, referecing number of people through. rework all == 1 to x > 0, and +=/-= val.
void sensor_check(int estimated_population) {
  if (Person_in_1 == 1) {
    delay(500);
    if ((Person_out_1 == 1)) {
      estimated_population += 1;
      Person_in_1 = 0;
      Person_out_1 = 0;

  } else if (Person_out_1 == 1) {
    delay(500);
    if ((Person_in_1 == 1)) {
      estimated_population -= 1;
      Person_in_1 = 0;
      Person_out_1 = 0;
  }
    }
  }
}