use std::io;
fn main() {
  let mut a=0;
  let mut b=1;
   println!("Please input your number.");
   let mut n = String::new();
   io::stdin().read_line(&mut n)
      .expect("Failed to read line");
   let nint : u32 = n
   .trim()
   .parse()
   .expect("Wanted a number");

   while nint>=b {
     b=a+b;
     a=b-a;
   }
   if a==nint {
     println!("{}",b-a+b)
   }
   else {
     println!("{}",a+b)
   }
}