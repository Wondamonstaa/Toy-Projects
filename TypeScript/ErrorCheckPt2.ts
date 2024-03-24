// Export => allow to use this function in other modules, if imported from the current module
export const somethingDangerous = () => {
  if (Math.random() > 0.5) {
    throw new Error("Oh dear!");
  }
};

try {
  somethingDangerous();
} catch (error) {
  if (error instanceof Error){
    console.log(error.message);
  }
}
