/*
Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
References

http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html


https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/c
*/

typedef struct Human_Cat_Dog_Years {
    unsigned human_years, cat_years, dog_years;
} years;

years human_years_cat_years_dog_years(unsigned human) {
  struct Human_Cat_Dog_Years y;
  y.human_years = human;
  switch (human) {
      case 1:     y.cat_years = 15; y.dog_years = 15; break;
      case 2:     y.cat_years = 24; y.dog_years = 24; break;
      default:    y.cat_years = 24 + (4 * (human - 2)); y.dog_years = 24 + (5 * (human - 2)); break;
  }
  
  return y;
}