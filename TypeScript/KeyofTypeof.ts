type Prices = {
  Apple?: number;
  Banana?: number;
  Orange?: number;
};

const productPrices= {
  Apple: 1.2,
  Banana: 0.5,
  Orange: 0.8,
} satisfies Prices;

export const getPrice = (productName: keyof typeof productPrices) => {
  return productPrices[productName] as Prices;
};
