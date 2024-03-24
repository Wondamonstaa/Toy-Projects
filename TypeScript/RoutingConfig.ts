type RoutingConfig = {
  routes: {
    path: string;
    component: string;
  }[];
};

const routingConfig = {
  routes: [
    {
      path: "home",
      component: "HomeComponent",
    },
    {
      path: "about",
      component: "1",
    },
    {
      path: "contact",
      component: "ContactComponent",
    },
  ],
} satisfies RoutingConfig;

const createRoutes = (config: {
  routes: {
    path: string;
    component: string;
  }[];
}) => {};

createRoutes(routingConfig);
