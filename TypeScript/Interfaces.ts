import { Equal, Expect } from "./helpers/type-utils";

interface Base {
  id: string;
};

interface User extends Base{
  firstName: string;
  lastName: string;
}

interface Post extends Base{
  title: string;
  body: string;
}

interface Comment extends Base{
  comment: string;
}

type tests = [
  Expect<Equal<User, { id: string; firstName: string; lastName: string }>>,
  Expect<Equal<Post, { id: string; title: string; body: string }>>,
  Expect<Equal<Comment, { id: string; comment: string }>>,
];
