/*
You are the best freelancer in the city. Everybody knows you, but what they don't know, is that you are actually offloading your work to other freelancers and and you rarely need to do any work. You're living the life!

To make this process easier you need to write a method called workNeeded to figure out how much time you need to contribute to a project.

Giving the amount of time in minutes needed to complete the project and an array of pair values representing other freelancers' time in [Hours, Minutes] format ie. [[2, 33], [3, 44]] calculate how much time you will need to contribute to the project (if at all) and return a string depending on the case.

If we need to contribute time to the project then return "I need to work x hour(s) and y minute(s)"
If we don't have to contribute any time to the project then return "Easy Money!"

https://www.codewars.com/kata/5b3e1dca3da310a4390000f3/train/cpp
*/

std::string workNeeded(int projectMinutes, std::vector<std::pair<int, int>> freelancers)
{
  int remainingWork{projectMinutes};
  for (size_t i=0;i<freelancers.size();++i) {
    remainingWork -= (freelancers[i].first * 60) + freelancers[i].second;
  }
  if (remainingWork <= 0)
    return "Easy Money!";
  else
    return std::string("I need to work ")
      + std::to_string(remainingWork / 60) + " hour(s) and "
      + std::to_string(remainingWork % 60) + " minute(s)";
}