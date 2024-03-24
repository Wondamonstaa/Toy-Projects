interface UserProfile {
  id: string;

  preferences: {
    //theme: "light" | "dark";
    theme: string;
  };
}

let user: UserProfile = {
  id: "123",
  preferences: {
    //theme: "blue",
    //theme: "light",
    theme: "dark"
  },
};
