#define led 3
#define knob A0
char serialData;
bool onoff = false;


void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available() > 0){
    serialData = Serial.read();
    if(serialData == '1'){
      while(serialData == '1'){
        int val = analogRead(knob);
        Serial.println(String(val));
        val = map(val, 1, 1024, 1, 255);
        analogWrite(led, val);
        delay(100);
        if(Serial.available() > 0){
          char flag = Serial.read();
          delay(100);
          if(flag == '0'){
            break;
            }
          else{
            continue;
            }
          }
        }
      }
  }
  
}