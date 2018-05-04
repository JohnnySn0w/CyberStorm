// steg so far. 

// ./steg -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
// ./steg -B -s -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg
// ./steg -B -r -o1024 -i256 -wnew.jpg > extracted.jpg
// above is what the command line will look like

#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

int sentinel[] = {0x0, 0xff, 0x0, 0x0, 0xff, 0x0};
int offset, interval;

void main (int argc, char* argv[])
{
	// gets offset value from command line by taking substring, converting to int
	char* num = argv[3];
	char *to = "-o";
	char *o = strtok(num, to);
	offset = atoi( o );
	num = argv[4];
	to = "-i";
	o = strtok(num, to);
	interval = atoi( o );
	
	//gets wrapper file name, wrapper file allocation 
	unsigned char* wrapper_file;
	if (strncmp(argv[5], "-w", 2) == 0)
    {
		int i = 5;
		argv[i] += 2;
		wrapper_file = (char*)malloc(strlen(argv[i]) + 1);
		strcpy(wrapper_file, argv[i]);
    }

	// opens file that matches variable above, and closes
	FILE* file_wrap = fopen(wrapper_file, "rb");
	fseek(file_wrap, 0, SEEK_END);
	// get size
	long wrap_size = ftell(file_wrap);
	fseek(file_wrap, 0, SEEK_SET);
	// Allocate memory/create bytearray from wrapper. make buffer -- reference: https://www.linuxquestions.org/questions/programming-9/how-to-read-jpg-image-in-c-708217/
	unsigned char* buffer_w =  (char *)malloc(wrap_size);
	fread(buffer_w, wrap_size, 1, file_wrap);
	fclose(file_wrap);
	
	int i=0;
	
	// store
	if (strcmp(argv[2], "-s") == 0)
	{
		int i = 0;
		
		if (argc <= 6)
		{
			printf("Cannot store - no file to hide.\n");
			exit(0);
		}
		//gets hidden file name by seeking substring beyond a certain token, coverting to FILE
		unsigned char* hidden_file;
		if (strncmp(argv[6], "-h", 2) == 0)
		{
			int i = 6;
			argv[i] += 2;
			hidden_file = (char*)malloc(strlen(argv[i]) + 1);
			strcpy(hidden_file, argv[i]);
		}

		// opens file that matches char* variable above, and closes
		FILE* file = fopen(hidden_file, "rb");
		
		// get size
		fseek(file, 0, SEEK_END);
		long hid_size = ftell(file);
		
		// put pointer back at beginning
		fseek(file, 0, SEEK_SET);
		
		// get header
		unsigned char* buffer =  (char *)malloc(hid_size);
		fread(buffer, hid_size, 1, file);
		fclose(file);


		// will execute for byte
		if (strcmp(argv[1], "-B") == 0) 
		{
			unsigned char* buffer_h =  (char *)malloc(wrap_size);
			while (i < hid_size)
			{
				buffer_w[offset] = buffer_h[i];
				offset += interval;
				i++;
				
			}
			
			i = 0;
			
			while (i < 6)
			{
				buffer_w[offset] = sentinel[i];
				offset += interval;
				i++;
			}
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
			/*
			for (int i=0; i < 6; i++)
			{
			}
			*/
			printf("this will be the bit function\n");
		}
			// if something incorrect is printed
		else
		{
			printf("%s is not a valid method type.\n", argv[1]);
			exit(0);
		}
		
		
	}
///////////////////////////////////////////////////////////////////////////////
	// retrieve
	else if (strcmp(argv[2], "-r") == 0)
	{
		int i = 0;
		unsigned char* buffer_h =  (char *)malloc(wrap_size);
		// will execute for byte
		if (strcmp(argv[1], "-B") == 0) 
		{
			while (offset < wrap_size)
			{
				buffer_h[i] = buffer_w[offset];
				offset += interval;
				i++;
			}
			// edits file we end up sending to
			FILE* file = freopen(NULL, "wb", stdout);
			fwrite(buffer_h, 1, wrap_size, file);
			fclose(file);
			/*
			while not at sentinel:
				if byte == sentinel[0]:
					for (i=0; i < 5; i++;)
					{
						skip interval
						have something here to reset if not matching sentinel
					}
				skip interval
				keep going to EOF
			sentinel hit; done
			*/
		}
		else if (strcmp(argv[1], "-b") == 0)
		{
			printf("this will be the bit function\n");
			
			while (offset < wrap_size)
			{
					
			}
			/*
			while not at sentinel:
				for (int i=0; i < 8; i++)
				{
					
				}
			*/
		}
		else
		{
			printf("%s is not a valid method type.\n", argv[1]);
			exit(0);
		}
		
	}

	else
	{
		printf("%s is not a valid method type.\n", argv[2]);
		exit(0);
	}
}
