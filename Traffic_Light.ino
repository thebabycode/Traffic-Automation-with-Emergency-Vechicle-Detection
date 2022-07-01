//Traffic Light code
int red_rg = 1, green_rg = 0;           // 0 for Red , 1 for Green in Road 1
int red_two = 14, green_two = 15;       //  for Road 2
int red_three = 18, green_three = 17;   // for Road 3


void setup() {
  pinMode(red_rg, OUTPUT);
  pinMode(green_rg, OUTPUT);

  pinMode(red_two, OUTPUT);
  pinMode(green_two , OUTPUT);

  pinMode(red_three , OUTPUT);
  pinMode(green_three , OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  // when ROAD 1 is GREEN
  digitalWrite(green_rg, HIGH);  
  digitalWrite(green_two, LOW); 
  digitalWrite(green_three, LOW);
  digitalWrite(red_rg, LOW);
  digitalWrite(red_two, HIGH); 
  digitalWrite(red_three, HIGH);
   
  delay(3000);     

  // when ROAD 2 is GREEN                  
  digitalWrite(green_rg, LOW);  
  digitalWrite(green_two, HIGH); 
  digitalWrite(green_three, LOW);
  digitalWrite(red_rg, HIGH);
  digitalWrite(red_two, LOW); 
  digitalWrite(red_three, HIGH); 
  
  delay(3000); 

  // when ROAD 3 is GREEN
  digitalWrite(green_rg, LOW);  
  digitalWrite(green_two, LOW); 
  digitalWrite(green_three, HIGH);
  digitalWrite(red_rg, HIGH);
  digitalWrite(red_two, HIGH); 
  digitalWrite(red_three, LOW);

  delay(3000);
}
