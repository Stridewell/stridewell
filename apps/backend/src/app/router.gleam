import app/web
import gleam/http.{Get, Post}
import gleam/string_builder
import wisp.{type Request, type Response}

pub fn handle_request(req: Request) -> Response {
  use req <- web.middleware(req)

  case wisp.path_segments(req) {
    [] -> home_page(req)

    ["api", "workouts"] -> workouts(req)

    _ -> wisp.not_found()
  }
}

fn home_page(req: Request) -> Response {
  use <- wisp.require_method(req, Get)

  let html = string_builder.from_string("Hello, Joe!")
  wisp.ok()
  |> wisp.html_body(html)
}

fn workouts(req: Request) -> Response {
  case req.method {
    Get -> list_workouts(req)
    Post -> create_workout(req)
    _ -> wisp.method_not_allowed([Get, Post])
  }
}

fn list_workouts(_req: Request) -> Response {
  let html = string_builder.from_string("These are your workouts")
  wisp.ok()
  |> wisp.html_body(html)
}

fn create_workout(_req: Request) -> Response {
  let html = string_builder.from_string("Your workout has been created")
  wisp.ok()
  |> wisp.html_body(html)
}
