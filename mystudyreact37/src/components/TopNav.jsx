import { Link } from 'react-router-dom';

function TopNav() {
  return (
    <div className="my-3">
      <ul className="flex gap-4">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/counter">counter</NavLink>
        </li>
        <li>
          <NavLink to="/reviews">reviews</NavLink>
        </li>
        <li>
          <NavLink to="/todos">todos</NavLink>
        </li>
      </ul>
    </div>
  );
}

function NavLink({ to, children }) {
  return (
    <Link
      to={to}
      className="pb-1 border-red-400 hover:border-b-4 duration-75 hover:text-red-400 text-sm"
    >
      {children}
    </Link>
  );
}

export default TopNav;
