import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import icon from '../../images/recipe-book.png'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div>
		{isLoaded && (
			<div className='nav'>
				<NavLink exact to="/">
					<img className="icon" src={icon} />
				</NavLink>
				<NavLink exact to="/recipes" className="nav-headers">Recipes</NavLink>
				<NavLink exact to="/collections" className="nav-headers">Collections</NavLink>
				{sessionUser && (
					<NavLink exact to="/grocerylist" className="nav-headers">Grocery List</NavLink>
				)}

				<ProfileButton user={sessionUser} />
			</div>
		)}
		</div>
	);
}

export default Navigation;
