function increasingTriplet(nums: number[]): boolean {

    let first: GLfloat = Infinity;
    let second: GLfloat = Infinity;

    for (let num of nums){
        
        if (num <= first){
            first = num;
        }
        else if (num <= second){
            second = num;
        }
        else{
            return true
        }
    }

    return false
};
