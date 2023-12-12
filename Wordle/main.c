/*
 Program 3: Best Wordle

 Created by:
    Name:	Kiryl Baravikou

 System:
    System Processor:	Apple M1
    System Memory:		8 GB
    System Version:		macOS 12.6 (21G115)
    Kernel Version:		Darwin 21.6.0


 Applications:
    Xcode:	14.0.1 (21336) (IDE)
    Clang:	14.0.0 (Complier)
    Replit:	~ (Testing)

 Date: Novemeber 4, 2022
*/

#include <setjmp.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define wordLength 5
#define fileSize 81
#define try
#define catch
#define throw

// Step 1: define a typedef struct to refer to the wordCountStruct using another
// name
typedef struct wordCountStruct allocator;
static jmp_buf exception;

struct wordCountStruct {

  int score; // Used to store the score
  char wordArray[81];
  // char *wordArray; // Used to store the words read from BOTH files
  int wordCounter;   // Used for word counting
  int *userFileSize; // Used for memory allocation
  int arraySize;     // Used for memory allocation
  int guesses;       // Used for counting guesses
  int answers;       // Used for counting answers
  int totalWords;    // Used to store the total number of words
  char *mallocArray;
  int lines;           // Used to store the total number of lines in a file
  char *answersMalloc; // Allocated array with answers
  char *guessesMalloc; // Allocated array with guesses
  char *allWord;       // Allocated array with answers + guesses
  // char word[wordSize + 1];
  char guessArray;
  char answerArray;
  int maxScore;
};

// Helper function: handles undesireable exceptions
void exceptionHandler();
// Helper function: uses qsort to sort the array in descending order by score +
// within the score - into ascending order alphabetically
void quicksort(allocator *allWord, size_t wordSize);
int thrower(char guessBuffer[], char answerBuffer[], int score, int pos,
            bool engine);
void sortPlusScore(allocator *allWord, allocator *wordOnes, int wordOnesLength,
                   int allWordLength, int gLen);

// Step 1: create compareFunction() => compares two words and their scores.
// If the scores are the same => words will be compared.
// Results => descending order by score + within score they are in alphabetic
// order. => DONE
int compareFunction(const void *a, const void *b) {

  int firstScore = ((allocator *)a)->score;
  int secondScore = ((allocator *)b)->score;

  if (firstScore != secondScore) {
    return secondScore - firstScore;
  } else {
    return strcmp(((allocator *)a)->wordArray, ((allocator *)b)->wordArray);
  }
}

// Step 2: create a quicksort() function => uses qsort to sort the array in
// descending order by score + within the score - into ascending order
// alphabetically => DONE
void quicksort(allocator *allWord, size_t wordSize) {

  if (wordSize < 0) {
    exceptionHandler();
  } else {
    qsort(allWord, wordSize, sizeof(allocator), compareFunction);
  }
}

// Step 3: create wordCounter() => allows to calculate the number of input lines
// => DONE
int wordCounter(char *filename) {

  char fileContents;
  char inputString[81];
  FILE *userFile = fopen(filename, "r");
  int words = 0;
  struct wordCountStruct counter;

  // Sanity check: ensure file open worked correctly
  if (userFile != NULL) {
    // Read the file contents until the end of the line will be reached +
    // increase the counter => DONE
    while (fscanf(userFile, "%s", inputString) != EOF) {
      words++;
      counter.lines++;
    }
  } else {
    printf("Error: could not open %s for reading\n", filename);
    exit(-1);
  }

  return words;
}

// Helper function: help
void contentLoader(char *answersFileName, char *guessesFileName) {

  FILE *userFileAnswers; // The file with answers
  FILE *userFileGuesses; // The file with guesses
  char answers[81];      // For reading the file contents from userFileAnswers
  char guesses[81];      // For reading the file contents from userFileGuesses
  char filename; // Our filename => I think we should use scanf() to get the
                 // filename via input
  struct wordCountStruct counter;  // Word counter
  struct wordCountStruct ourArray; // Will be used for allocating the memory =>
                                   // int* userFileSize inside the struct
  counter.wordCounter = 0;         // The initial value of the counter is 0

  /*Step 1: Open the files in turn and read the words in them one at a time
  until you reach the end of the file.
  Increment a counter as you do this so you know how many words there are in
  each file.*/

  // Step 1: open the file with guesses => DONE
  userFileGuesses =
      fopen(guessesFileName, "r"); // Connect logical name to filename

  // Step 2: open the file with answers => DONE
  userFileAnswers =
      fopen(answersFileName, "r"); // Connect logical name to filename

  /*Here we check if the GUESSES file is actually opened => DONE*/
  if (userFileGuesses == NULL) {
    printf("Error: could not open %s for reading\n",
           guesses); // Here we must use the actual filename
    exit(-1);
  }

  /*Here we check if the ANSWERS file is actually opened => DONE*/
  if (userFileAnswers == NULL) {
    printf("Error: could not open %s for reading\n",
           answers); // Here we must use the actual filename
    exit(-1);
  }

  // Read + count the GUESSES => DONE
  while (fscanf(userFileGuesses, "%s", guesses) != EOF) {
    // Count the number of input words in userFileGuesses => store in the common
    // counter => DONE
    int size = counter.wordCounter++;
    // Allocate the memory inside the array located in the struct
    ourArray.userFileSize = (int *)malloc(size * sizeof(userFileGuesses));
    // Increase the size_t to know the actual array's size
    ourArray.arraySize++;
    counter.answers++;
  }

  // Read + count the ANSWERS => DONE
  while (fscanf(userFileAnswers, "%s", answers) != EOF) {

    // Count the number of input words in userFileAnswers => store in the common
    // counter => DONE
    int size = counter.wordCounter++;
    // Allocate the memory inside the array located in the struct
    ourArray.userFileSize = (int *)malloc(size * sizeof(userFileAnswers));
    // Increase the size_t to know the actual array's size
    ourArray.arraySize++;
    counter.guesses++;
  }

  /*Close the files*/
  fclose(userFileGuesses);
  fclose(userFileAnswers);

  free(ourArray.wordArray);
}

// Helper function to open the file for the second time using the same procedure
// and algorithm
int teleport(allocator *allWord, char *guessesFileName, char *answersFileName) {

  char filename[fileSize];
  char userInput[fileSize];
  FILE *userFile;
  int pos = 0;

  userFile = fopen(filename, "r");

  // Check if the file was opened
  if (userFile == NULL) {
    exceptionHandler();
    exit(-1);
  } else {
    while (fscanf(userFile, "%s", userInput) != EOF) {
      // Transit usertInput inside the allocated array
      strncpy(allWord[pos].wordArray, userInput, fileSize - 1);
      allWord[pos].score = 0;
      pos++;
    }

    // Close the file
    fclose(userFile);
  }
}

// Step 4: create the fileReader() function => accepts the allocated array and
// two filenames with guesses + anwers
void fileReader(allocator *allWord, char *guessesFileName,
                char *answersFileName) {

  // Step 1: declare the variables
  char filename[81];
  char userInput[81];
  FILE *userFile;
  int pos = 0;
  FILE *userFileAnswers; // The file with answers
  FILE *userFileGuesses; // The file with guesses
  char answers[81];      // For reading the file contents from userFileAnswers
  char guesses[81];      // For reading the file contents from userFileGuesses
  struct wordCountStruct counter;  // Word counter
  struct wordCountStruct ourArray; // Will be used for allocating the memory =>
                                   // int* userFileSize inside the struct

  // Step 2: transfer the contents of guesses file inside the file for reading
  strcpy(filename, guessesFileName);

// Step 3: open the filename and stream its contents inside userFile (Credit: TA
// OH)
driver:
  userFile = fopen(filename, "r");

  // Step 4: check if the file was opened => sanity check
  if (userFile == NULL) {
    exceptionHandler();
    exit(-1);
  } else {
    // Read the file contents until the end of the file
    while (fscanf(userFile, "%s", userInput) != EOF) {
      // Transit usertInput inside the allocated array
      strncpy(allWord[pos].wordArray, userInput, 80);
      // Drop the score and move next
      allWord[pos].score = 0;
      pos++;
    }

    // Close the file
    fclose(userFile);
    if (strcmp(filename, answersFileName) == 0) {
      return;
    } else {
      strncpy(filename, answersFileName, 80);
      goto driver;
      teleport(&allWord, &guessesFileName, &answersFileName);
    }
  }
}

// Step 5: create eraser() function => deletes character at the specified
// position if there is a match between the source and the target arrays at the
// current index => replacing the match with the space according to the
// program's description
void eraser(char *wordOne, char *answerWord) {

  size_t i = 0;
  size_t j = 0;

  // Credit: Professor Reed's solution
  for (i = 0; i < wordLength; i++) {
    if (wordOne[i] == answerWord[i]) {
      answerWord[i] = ' ';
      continue;
    }

    for (j = 0; j < wordLength; j++) {
      // if a letter from first word is the same and is in the exact position of
      // a letter in answer, set that letter blank in answer.
      if (wordOne[i] == answerWord[j]) {
        answerWord[j] = ' ';
        break;
      }
    }
  }
}

// Helper function for calculateScore() => checks if two chars are equal => then
// updates the score accordingly by 1 point
int positionChecker(char guesses[], char answers[], int score, bool engine) {

  struct wordCountStruct object;
  object.guesses;
  object.answers;
  size_t i = 0;
  size_t j = 0;

  for (unsigned int i = 0; i < wordLength; i++) {
    for (unsigned j = 0; j < wordLength; j++) {
      // If there is a match => increment the score by 1
      if (guesses[i] == answers[j]) {
        score += 1;
        guesses[i] = '-';
        object.score += 1;
        answers[j] = '/';
      } else {
        // exceptionHandler();
      }
    }
  }

  return score;
}

// Step 6:  helper function for calculateScore() => checks if two chars are
// equal => then updates the score accordingly by 3 points
int equilizer(char guesses[], char answers[], int score) {

  bool engine = true;
  size_t j = 0;
  int pos = 0;
  size_t i = 0;
  do {
    // Check if the char at the specified index inside the guesses array mathes
    // the char inside the answers at the same index
    if (guesses[i] == answers[i]) {
      // If there is a match => increase the score by 3 points
      score = thrower(guesses, answers, score, i, engine);
    }
    i++;
  } while (i != wordLength);

  score = positionChecker(guesses, answers, score, engine);

  return score;
}

// Step 7: helper function for handling exceptions
int thrower(char guesses[], char answers[], int score, int pos, bool engine) {

  if (engine) {
    // longjmp(exception, 555);
    score += 3;
    guesses[pos] = '-';
    answers[pos] = '_';
  } else {
    score = score;
  }
  return score;
}

// Step 8: create a function to calculate the best score
// Step through each word in the array of all the words, computing its score as
// you compare against all answer words, accumulating points when letters match.
// When a letter matches and is also in the correct position add 3 points.  When
// a letter matches but is not in the correct position add 1 point.
int calculateScore(char *guessWord, char *answerWord, allocator *wordOne) {

  int score = 0;
  char guesses[wordLength + 1];
  struct wordCountStruct object;
  char answers[wordLength + 1];
  object.answerArray;
  object.guessArray;
  bool engine = true;

  strcpy(guesses, guessWord);
  strcpy(answers, answerWord);

  // Special case used for debugging purposes (@Credit: Professor Reed)
  if (wordOne) {
    eraser(wordOne->wordArray, answers);
  } else {
    // exceptionHandler();
  }

  score = equilizer(guesses, answers, score);
  return score;
}

// Step 9: Helper function to handle the exception => DONE
void exceptionHandler() {
  printf("Invalid number accepted!");
  printf("\n");
  printf("ExceptionHandler: terminating the program!");
  exit(0);
}

// Step 10: create a scoreEvaluator() that calculates the total score for all
// the words located in the allocated array => DONE
void scoreEvaluator(allocator *allWord, int allWordLength, int gLen,
                    allocator *wordOne) {

  struct wordCountStruct object;
  size_t i = 0;

  if (allWordLength == 0) {
    exceptionHandler();
  } else {
    do {
      size_t j = gLen;
      do {
        if (1) {
          char *unitGuess = object.guessesMalloc = allWord[i].wordArray;
          char *unitAnswer = object.answersMalloc = allWord[j].wordArray;
          object.wordCounter += calculateScore(unitGuess, unitAnswer, wordOne);
          ++j;
        } else {
          exceptionHandler();
        }

      } while (j < allWordLength);

      allWord[i].score = object.wordCounter;
      object.wordCounter = 0;

      ++i;

    } while (i < allWordLength);
  }
}

// Step 11: Helper function: used to clean the allocated memory => DONE
void memoryCleaner(allocator *word) {

  size_t j = 0;
  size_t size = sizeof(word);
  do {
    free(word);
    // word[j] = 0;
    j++;
  } while (j < 1);

  word = NULL;
}

// Helper function for the end of the game => frees the memory + sorts all the
// words inside arrays + evaluates the scores
void finalLoader(allocator *allWord, char guessesFileName[],
                 char answersFileName[], allocator *wordOnes,
                 int wordOnesLength, int allWordLength, int guess) {

  printf("\n");
  printf("Words and scores for top first words and second words:");
  printf("\n");
  fileReader(allWord, guessesFileName, answersFileName);
  sortPlusScore(allWord, wordOnes, wordOnesLength, allWordLength, guess);
  printf("Done\n");
  memoryCleaner(allWord);
  memoryCleaner(wordOnes);
}

// Step 12: helper function to determine the maximum score
int topCalculator(allocator *wordOne, allocator *wordOnes, int index,
                  allocator *answers, int allWordLength, int gLen,
                  allocator *allWord) {

  struct wordCountStruct object;
  object.maxScore = 0;

  if (index < 0) {
    exceptionHandler();
    return 0;
  } else {
    wordOne = wordOnes + index;
    memcpy(answers, allWord, allWordLength * sizeof(allocator));
    scoreEvaluator(answers, allWordLength, gLen, wordOne);
    printf("%s %d\n", *&wordOne->wordArray, *&wordOne->score);
    quicksort(answers, allWordLength);
    object.maxScore = answers->score;
  }

  return object.maxScore;
}

// Step 13: helper function to help sorting the scores of the second best word
// => DONE
void sortPlusScore(allocator *allWord, allocator *wordOnes, int wordOnesLength,
                   int allWordLength, int gLen) {

  allocator *wordOne;
  allocator *answers = malloc(allWordLength * sizeof(allocator));
  struct wordCountStruct object;
  object.guesses;
  object.answers;
  size_t i = 0;
  size_t j = 0;

  do {
    int topScore = topCalculator(wordOne, wordOnes, i, answers, allWordLength,
                                 gLen, allWord);
    for (unsigned int i = 0; i < allWordLength; i++) {
      if (answers[i].score != topScore) {
        break;
      }
      printf("   %s %d", answers[i].wordArray, answers[i].score);
    }
    printf("\n");
    ++i;

  } while (i < wordOnesLength);

  // Free the memory using the helper function
  memoryCleaner(answers);
}

// Helper function for main
void packageBuilder(allocator *allWord, char answersFileName[],
                    char guessesFileName[], int allWordLength, int guess,
                    int answer) {

  fileReader(allWord, guessesFileName, answersFileName);
  scoreEvaluator(allWord, allWordLength, guess, NULL);
  quicksort(allWord, allWordLength);
}

// Step 15: finish main()
int main() {

  char answersFileName[fileSize] = "answersTiny.txt";
  char guessesFileName[fileSize] = "guessesTiny.txt";
  char answersFileNameStorage[fileSize];
  char guessesFileNameStorage[fileSize];
  int allWordLength;
  int wordOnesLength = 0;
  allocator *allWord;
  int menuOption = 0;

  struct wordCountStruct object;
  int guess = object.guesses = wordCounter(guessesFileName);
  int answer = object.answers = wordCounter(answersFileName);
  allWordLength = answer + guess;

  printf("Default file names are %s and %s\n", answersFileName,
         guessesFileName);

  // Display the menu
  do {
    printf("\n");
    printf("Menu Options:\n");
    printf("  1. Display best first words only\n");
    printf("  2. Display best first and best second words\n");
    printf("  3. Change answers and guesses filenames\n");
    printf("  4. Exit\n");
    printf("Your choice: ");
    scanf("%d", &menuOption);

    if (menuOption == 4) {
      exit(1);
    } else if (menuOption == 3) {
      // Change file names.  Menu will then be redisplayed.
      printf("Enter new answers and guesses filenames: ");
      scanf("%s %s", answersFileName, guessesFileName);
    } else if (menuOption == 1) {
      printf("%s has %d words\n", answersFileName, answer);
      printf("%s has %d words\n", guessesFileName, guess);

      printf("\nWords and scores for top first words:\n");
    }

  } while (menuOption == 3);

  // Allocate memory for each file that will be transferred to the allocated
  // array
  for (int j = 0; j < allWordLength; j++) {
    allWord = malloc(allWordLength * sizeof(allocator));
  }

  packageBuilder(allWord, answersFileName, guessesFileName, allWordLength,
                 guess, answer);

  int topScore = allWord->score;
  int i = 0;
  do {
    if (allWord[i].score != topScore) {
      break;
    }
    wordOnesLength++;
    if (menuOption == 1) {
      printf("%s %d\n", allWord[i].wordArray, allWord[i].score);
    }
    i++;
  } while (i < allWordLength);

  if (menuOption == 1) {
    printf("Done\n");
    memoryCleaner(allWord);
    return 0;
  }

  allocator *wordOnes = malloc(wordOnesLength * sizeof(allocator));
  int k = 0;
  do {
    wordOnes[k] = allWord[k];
    k++;

  } while (k < wordOnesLength);

  // Finishes the game with final steps + frees the memory => DONE
  finalLoader(allWord, guessesFileName, answersFileName, wordOnes,
              wordOnesLength, allWordLength, guess);

  return 0;
}
