import { expect, it } from "vitest";

const tryCatchDemo = (state: "fail" | "succeed") => {
  try {
    if (state === "fail") {
      throw new Error("Failure!");
    }
  //} catch (e: any) {
    // Option 1
    //return e.message;

    // Option 2
    //return (e as Error).message;
  } catch (e) {
    if (e instanceof Error){
      return e.message;
    }
  }
};

it("Should return the message when it fails", () => {
  expect(tryCatchDemo("fail")).toEqual("Failure!");
});
