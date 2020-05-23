#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<time.h>




int hour = 0, minutes = 0 , seconds = 0;

void * calc_hour(){
	
	while(1){
		
		if(minutes == 60){
			
			minutes  = 0;
			seconds  = 0;
		    if(hour == 24){
				hour = 0; 			
			}
			else{
				hour++;
			}
					
		}	
		
	}
		
}

void * calc_min(){
	
	while(1){

		if(seconds == 60){
			
			minutes ++;
			seconds = 0;	
		}
		
	}
	
}

void * calc_sec(){


	while(1){
		
		if(seconds != 60){
			sleep(1);
			seconds++;	
		}
		
	}
}



void * display(){

	pthread_t thour, tmin, tsec;
	
	pthread_create(&tsec, NULL, calc_sec, NULL);
	pthread_create(&tmin, NULL, calc_min, NULL);
	pthread_create(&thour, NULL, calc_hour, NULL);
	
	while(1){
		
		printf("\r %02d : %02d : %02d", hour, minutes, seconds);	
	}

	// wait for the threads to execute
	pthread_join(tsec, NULL);
	pthread_join(tmin, NULL);
	pthread_join(thour, NULL);
	
	return NULL;		
}


int main(int argc, char * argv[]){
	
	time_t now;
	time(&now);

	

	struct tm *local_time = localtime(&now);

	// systems local time
	hour = local_time -> tm_hour;
	minutes = local_time -> tm_min;
	seconds = local_time -> tm_sec;
	
	pthread_t tmain;
	
	pthread_create(&tmain, NULL, display, NULL );
	pthread_join(tmain, NULL);

	return 0;
}

