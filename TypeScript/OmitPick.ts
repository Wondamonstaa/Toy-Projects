import { Equal, Expect } from "./helpers/type-utils";

interface User {
  id: string;
  firstName: string;
  lastName: string;
}

/**
 * How do we create a new object type with _only_ the
 * firstName and lastName properties of User?
 */

// Option 1
type MyType = Omit<User, "id">;

// Option 2
//type MyType = Pick<User, "firstName" | "lastName">;


type tests = [Expect<Equal<MyType, { firstName: string; lastName: string }>>];
