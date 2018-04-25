// steg so far. 

// ./steg -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
// ./steg -B -s -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg
// ./steg -B -r -o1024 -i256 -wnew.jpg > extracted.jpg
// above is what the command line will look like

#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

int sentinel[] = {0x0, 0xff, 0x0, 0x0, 0xff, 0x0};

void main (int argc, char* argv[])
{
	// update: not doing separate functions for bit/byte. Gonna use a lot of if statements in main. It's easier that way.
	
	if (argc <= 6)
	{
		printf("Note: enough arguments to retrieve, but not to store.\n\n");
	}
	
	// gets offset value from command line by taking substring, converting to int
	//note: atol is for long. this is just a note to myself
	char* num = argv[3];
	char *to = "-o";
	char *o = strtok(num, to);
	int offset = atoi( o );


	// gets interval value from command line by taking substring, converting to int
	char* mun = argv[4];
	char *ot = "-i";
	char *i = strtok(mun, ot);
	int interval = atoi( i );

	
	//gets wrapper file name by seeking substring beyond a certain token, coverting to FILE
	char* wraps = argv[5];
	char *w = "-w";
	char* wrapper = strtok(wraps, w);

	// opens file that matches char* variable above, and closes
	//FILE* file_wrap = fopen(wrapper, "rb");
	//fseek(file_wrap, 0, SEEK_END);
	//long wrap_size = ftell(file_wrap);
	//fseek(file_wrap, 0, SEEK_SET);
	//fclose(file_wrap);
	
	// store
	if (strcmp(argv[2], "-s") == 0)
	{
		int i = 0;
		
		if (argc <= 6)
		{
			printf("Cannot store - no file to hide.\n");
			//exit
		}
		else
			printf("Current mode: Storage\n");
		//gets hidden file name by seeking substring beyond a certain token, coverting to FILE
		char* hide = argv[6];
		char *h = "-h";
		char* hidden = strtok(hide, h);

		// opens file that matches char* variable above, and closes
		//FILE* file_hide = fopen(hidden, "rb");
		//fseek(file_hide, 0, SEEK_END);
		//long hid_size = ftell(file_hide);
		//fseek(file_hide, 0, SEEK_SET);


		// will execute for byte
		if (strcmp(argv[1], "-B") == 0) 
		{
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
///////////////////////////////////////////////////////////////////////////////
	// retrieve
	else if (strcmp(argv[2], "-r") == 0)
	{
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
		
		printf("Current mode: Retrieval\n");
	}

	else
		printf("%s is not a valid method type.\n", argv[2]);
}
