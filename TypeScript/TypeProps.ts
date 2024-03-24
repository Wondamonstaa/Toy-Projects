// Option 1
type User = {
    name: string;
    age?: number;
};

// Option 2
/*const user: Record<string, number | string> = {
  name: "Matt",
};
user.adsdsadsa = "1";
*/

const user: User = {
  name: "Matt",
};

user.age = 24;
