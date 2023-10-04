


type expr = 
| Num of int
| Add of expr * expr
| Sub of expr * expr
| Mul of expr * expr
| Div of expr * expr
| Mod of expr * expr
;;
(*
let rec format e = 
    match e with
    | Num n -> Printf.sprintf "%d" n
    | Add (a, b) -> Printf.sprintf "(%s + %s)" (format a) (format b)
    | Sub (a, b) -> Printf.sprintf "(%s - %s)" (format a) (format b)
    | Mul (a, b) -> Printf.sprintf "(%s * %s)" (format a) (format b)
    | Div (a, b) -> Printf.sprintf "(%s / %s)" (format a) (format b)
    | Mod (a, b) -> Printf.sprintf "(%s mod %s)" (format a) (format b)
;;

*)
(*
let rec format e = 
    match e with
    | Num n -> Printf.sprintf "%d" n
    | Add (a, b) -> Printf.sprintf "%s + %s" (format a) (format b)
    | Sub (a, b) -> Printf.sprintf "%s - %s" (format a) (format b)
    | Mul (a, b) ->
        match a with
        | Num _ ->
            match b with
            | Add (_, _) | Sub (_, _) -> Printf.sprintf "%s * (%s)" (format a) (format b)
            | _ -> Printf.sprintf "%s * %s" (format a) (format b)
        | Add (_, _) | Sub (_, _) ->
            match b with
            | Num _ -> Printf.sprintf "(%s) * %s" (format a) (format b)
            | Add (_, _) | Sub (_, _) -> Printf.sprintf "(%s) * (%s)" (format a) (format b)
            | _ -> Printf.sprintf "%s * %s" (format a) (format b)
        | _ -> Printf.sprintf "%s * %s" (format a) (format b)
    

    | Div (a, b) -> Printf.sprintf "(%s / %s)" (format a) (format b)
    | Mod (a, b) -> Printf.sprintf "(%s mod %s)" (format a) (format b)
;;
*)



let rec format e = 
    match e with
    | Num n -> Printf.sprintf "%d" n
    | Add (a, b) -> Printf.sprintf "%s + %s" (format a) (format b)
    | Sub (a, b) -> Printf.sprintf "%s - %s" (format a) (format b)
    | Mul (a, b) ->
        match a with
        | Num _ ->
            match b with
            | Add (_, _) | Sub (_, _) -> Printf.sprintf "%s * (%s)" (format a) (format b)
            | _ -> Printf.sprintf "%s * %s" (format a) (format b)
        | Add (_, _) | Sub (_, _) ->
            match b with
            | Num _ -> Printf.sprintf "(%s) * %s" (format a) (format b)
            | Add (_, _) | Sub (_, _) -> Printf.sprintf "(%s) * (%s)" (format a) (format b)
            | _ -> Printf.sprintf "%s * %s" (format a) (format b)
        | _ -> Printf.sprintf "%s * %s" (format a) (format b)
    

    | Div (a, b) -> Printf.sprintf "(%s / %s)" (format a) (format b)
    | Mod (a, b) -> Printf.sprintf "(%s mod %s)" (format a) (format b)
;;






let rec eval e =
    match e with
    | Num n -> n
    | Add (a, b) -> eval(a) + eval(b)
    | Sub (a, b) -> eval(a) - eval(b)
    | Mul (a, b) -> eval(a) * eval(b)
    | Div (a, b) -> eval(a) / eval(b)
    | Mod (a, b) -> eval(a) mod eval(b)
;;


let formatIntoEval e = format e ^ " = " ^ format(Num (eval e))
;;


(*
let e = Sub(Add(Mul(Mod(Num 8, Num 3), Num 2), Num 3), Num 4)
;;
*)
(*
let e = Mul(Num 3, Add(Num 9, Num 8))
;;
*)

(*
print_endline(formatIntoEval e)
;;
*)

let e = Mul (Num 1, Add (Num 2, Num 3))
;;

let e1 = Add (Num 1, Add (Num 2, Num 3))
;;
let e2 = Add (Num 1, Mul (Num 2, Num 3))
;;
let e3 = Mul (Num 1, Add (Num 2, Sub (Num 3, Num 4)))
;;

print_endline(format e)
;;

print_endline(format e1)
;;
print_endline(format e2)
;;
print_endline(format e3)
;;


