interface LukeSkywalker {
  name: string;
  height: string;
  mass: string;
  hair_color: string;
  skin_color: string;
  eye_color: string;
  birth_year: string;
  gender: string;
}

// First Option
export const fetchLukeSkywalker = async (): Promise<LukeSkywalker> => {
  const data = await fetch("https://swapi.dev/api/people/1").then((res) => {
    return res.json();
  });

  return data;
};

// Second Option
export const fetchLukeSkywalker = async () => {
  const data: LukeSkywalker = await fetch("https://swapi.dev/api/people/1").then((res) => {
    return res.json();
  });

  return data;
};

// Will work now
// data.name ... data.mass etc.

// Third Option
export const fetchLukeSkywalker = async () => {
  const data = await fetch("https://swapi.dev/api/people/1").then((res) => {
    return res.json();
  });

  // const matt = {} as LukeSkywalker; => this is the stronger way to tell TS about the type of the object
  
  return data as LukeSkywalker;
};
