


type expr = 
| Num of int
| Add of expr * expr
| Diff of expr * expr
| Prod of expr * expr
| Quot of expr * expr
| Mod of expr * expr
;;

let rec format e = 
    match e with
        | Num n -> Printf.sprintf "%d" n
        | Add (a, b) -> Printf.sprintf "(%s + %s)" (format a) (format b)
        | Diff (a, b) -> Printf.sprintf "(%s - %s)" (format a) (format b)
        | Prod (a, b) -> Printf.sprintf "(%s * %s)" (format a) (format b)
        | Quot (a, b) -> Printf.sprintf "(%s / %s)" (format a) (format b)
        | Mod (a, b) -> Printf.sprintf "(%s mod %s)" (format a) (format b)
;;

let rec eval e =
    match e with
        | Num n -> n
        | Add (a, b) -> eval(a) + eval(b)
        | Diff (a, b) -> eval(a) - eval(b)
        | Prod (a, b) -> eval(a) * eval(b)
        | Quot (a, b) -> eval(a) / eval(b)
        | Mod (a, b) -> eval(a) mod eval(b)
;;


let evalIntoFormat e = format e ^ " = " ^ format(Num (eval e))
;;



let e = Diff(Add(Prod(Mod(Num 8, Num 3), Num 2), Num 3), Num 4)
;;
let e = Prod(Num 3, Add(Num 9, Num 8))
;;

print_endline(evalIntoFormat e)
;;





