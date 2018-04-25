// steg so far. 

// ./steg -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
// ./steg -B -s -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg
// ./steg -B -r -o1024 -i256 -wnew.jpg > extracted.jpg
// above is what the command line will look like


//stuff to include libraries for certain functions, esp. math and system arguments and image stuff

//#include <iostream>
#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
//#include <math.h>

int sentinel[] = {0x0, 0xff, 0x0, 0x0, 0xff, 0x0};
char* buffer_wrap;
char* buffer_hide;

void main (int argc, char* argv[])
{
	// update: not doing separate functions for bit/byte. Gonna use a lot of if statements in main. It's easier that way.
	
	if (argc < 6)
	{
		printf("Not enough arguments.\n\n");
		//return(0);
	}
	
	// gets offset value from command line by taking substring, converting to int
	//note: atol is for long. this is just a note to myself
	char* num = argv[3];
	char *to = "-o";
	char *o = strtok(num, to);
	int offset = atoi( o );
	printf("offset: %d\n", offset);

	// gets interval value from command line by taking substring, converting to int
	char* mun = argv[4];
	char *ot = "-i";
	char *i = strtok(mun, ot);
	int interval = atoi( i );
	printf("interval: %d\n", interval);
	
	//gets wrapper file name by seeking substring beyond a certain token, coverting to FILE
	char* wraps = argv[5];
	char *w = "-w";
	char* wrapper = strtok(wraps, w);
	printf("%s\n", wrapper);
	// opens file that matches char* variable above, and closes currently
	//FILE* file_wrap = fopen(wrapper, "rb+");
	//fclose(file_wrap);
	
		//gets hidden file name by seeking substring beyond a certain token, coverting to FILE
	char* hide = argv[6];
	char *h = "-h";
	char* hi = strtok(hide, h);
	printf("%s\n", hi);
	// opens file that matches char* variable above, and closes
	//FILE* hidden = fopen(hi, "rb+");
	//fclose(hidden);
	
		// store
		if (strcmp(argv[2], "-s") == 0)
		{
			printf("Storage\n");
			int i = 0;
				
			// will execute for byte
			if (strcmp(argv[1], "-B") == 0) 
			{
				//for (int i=0; i < argc; i++)
				//	printf("%s\n",argv[i]);

				/*
				while i < length(H)
				{
					W[o] = H[i];
					offset += interval;
					i++;
				}

				int i = 0;
				while i < length(sentinel)
				{
					W[o] = S[i];
					offset += interval;
					i++
				}
				*/
				printf("This will be the byte function\n");
			}
			//execute for bit
			else if (strcmp(argv[1], "-b") == 0)
			{
				/*
				i = 0;
				j = 0;
				while j < length(H):
					for k = 0..7:
						W[i] &= 11111110
						W[i] |= ((H[j] & 10000000 >> 7))
						H[j] <<= 1
						i += I
					j++
				end while
				*/
				printf("this will be the bit function\n");
			}
				// if something incorrect is printed
			else
				printf("%s is not a valid method type.\n", argv[1]);
		}
		
		// retrieve
		else if (strcmp(argv[2], "-r") == 0)
		{
			printf("Retrieval\n");
			int i = 0;
			// put more here
			// will execute for byte
			if (strcmp(argv[1], "-B") == 0) 
			{
				printf("This will be the byte function\n");
			}
			else if (strcmp(argv[1], "-b") == 0)
			{
				printf("this will be the bit function\n");
			}
			else
				printf("%s is not a valid method type.\n", argv[1]);
		}
		
		else
			printf("%s is not a valid method type.\n", argv[2]);
			
		
}
