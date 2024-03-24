import { expect, it } from "vitest";

type CacheType = {
  [index: string]: string;
}

const createCache = () => {

  // Option 1
  const cache: CacheType = {};

  // Option 2
  // const cache: Record<string, string> = {};

  // Option 3
  /*const cache: {
    [index: number]: string;
  } = {}*/

  const add = (id: string, value: string) => {
    cache[id] = value;
    //cache[1] = "StringValue1"
  };

  const remove = (id: string) => {
    delete cache[id];
  };

  return {
    cache,
    add,
    remove,
  };
};

it("Should add values to the cache", () => {
  const cache = createCache();

  cache.add("123", "Matt");

  expect(cache.cache["123"]).toEqual("Matt");
});

it("Should remove values from the cache", () => {
  const cache = createCache();

  cache.add("123", "Matt");
  cache.remove("123");

  expect(cache.cache["123"]).toEqual(undefined);
});
