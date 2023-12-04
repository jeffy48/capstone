import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { NavLink, useHistory } from 'react-router-dom';
import { logout } from "../../store/session";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    closeMenu()
    history.push("/")
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu}>
        <i className="fas fa-user-circle" />
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <p>Hello, {user.username}</p>
            <NavLink exact to="/myrecipes">My Recipes</NavLink>
            <NavLink exact to="/mycollections">My Collections</NavLink>
            <NavLink exact to="/myreviews">My Reviews</NavLink>
            <button onClick={handleLogout}>Log Out</button>
          </>
        ) : (
          <>
            <NavLink exact to="/login">Login</NavLink>
            <NavLink exact to="/signup">Sign Up</NavLink>
            {/* <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />

            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            /> */}
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
