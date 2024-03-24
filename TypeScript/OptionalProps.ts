import { expect, it } from "vitest";
import { ZodOptional, ZodOptionalType } from "zod";

type Object = {
    first: string,
    last?: string | undefined
};

export const getName = (params: Object) => {
  if (params.last) {
    return `${params.first} ${params.last}`;
  }
  return params.first;
};

it("Should work with just the first name", () => {
  const name = getName({
    first: "Matt",
    //last: ""
  });

  expect(name).toEqual("Matt");
});

it("Should work with the first and last name", () => {
  const name = getName({
    first: "Matt",
    last: "Pocock",
  });

  expect(name).toEqual("Matt Pocock");
});
