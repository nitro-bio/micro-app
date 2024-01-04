import { useEffect, useState } from "react";

type User = {
  id: number;
  name: string;
  email: string;
};

function App() {
  const [users, setUsers] = useState<User[]>([]);
  useEffect(function fetchUsers() {
    fetch("/api/users")
      .then((res) => res.json())
      .then((data) =>
        setUsers(
          data.users.map((user: [number, string, string]) => {
            return {
              id: user[0],
              name: user[1],
              email: user[2],
            };
          }),
        ),
      );
  }, []);

  return (
    <div className="min-h-screen bg-zinc-800 px-8 py-6 text-zinc-100">
      <h1 className="text-4xl">Users (fetched from Backend)</h1>
      <ul className="mt-4 flex flex-col gap-2">
        {users.map((user: User) => (
          <li key={user.id} className="text-2xl text-sky-300">
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
